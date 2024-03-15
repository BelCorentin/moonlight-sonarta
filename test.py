from sonar.inference_pipelines.speech import SpeechToTextModelPipeline
import librosa    
import soundfile as sf


y, s = librosa.load('hello.wav', sr=16000) # Downsample 44.1kHz to 8kHz

output_path = 'output.wav'
sf.write(output_path, y, 16000)

s2t_model = SpeechToTextModelPipeline(encoder="sonar_speech_encoder_eng",
                                      decoder="text_sonar_basic_decoder",
                                      tokenizer="text_sonar_basic_decoder")

import torchaudio
inp, sr = torchaudio.load("output.wav")
assert sr == 16000, "Sample rate should be 16kHz"

# passing loaded audio files
prediction = s2t_model.predict([inp], target_lang="eng_Latn")
print(prediction)
# ['Television reports show white smoke coming from the plant.']

# passing multiple wav files 
# s2t_model.predict(["./tests/integration_tests/data/audio_files/audio_1.wav",
#                    "./tests/integration_tests/data/audio_files/audio_2.wav"], target_lang="eng_Latn")
# ['Television reports show white smoke coming from the plant.',
# 'These couples may choose to make an adoption plan for their baby.']