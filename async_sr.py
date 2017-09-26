import argparse
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'myproject1.json'

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=8000,
        language_code='fr-FR')

    operation = client.long_running_recognize(config, audio)
    print(operation)
    print('Waiting for operation to complete...')
    response = operation.result(timeout=1000)

    # Print the first alternative of all the consecutive results.
    for result in response.results:
        trans = unicode(result.alternatives[0],'utf-8')
        conf = unicode(result.alternatives[0].confidence,'utf-8')
        print('Transcript:{}'.format(trans))
        print('Confidence: {}'.format(conf))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('speech_file', help = 'Full path of audio file to be recognized')
    args = parser.parse_args()
    uri = 'gs://audio_project_database/ongcloud/' + args.speech_file
    print(uri)
    transcribe_gcs(uri)
