from azure.cognitiveservices.speech import  SpeechConfig, SpeechSynthesizer, AudioConfig, ResultReason

def synthesize_speech(text, voice_name='voice_name', filename='output_filename', subscription_key='subscription_key', region='region'):
    speech_config = SpeechConfig(subscription=subscription_key, region=region)
    audio_config = AudioConfig(filename=filename)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()
    if result.reason == ResultReason.SynthesizingAudioCompleted:
        print("Synthesis succeeded.")
    else:
        print(f"Synthesis failed. Error: {result.error_details}")
    return result
