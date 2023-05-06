import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, send_file)
from emoailib.text_to_speech import synthesize_speech

app = Flask(__name__)



@app.route('/synthesize', methods=['POST'])
def synthesize_route():
    subscription_key = "998723bccc394ddb89b2ffe73bb91651"
    region = "eastus"
    text = request.form['text']
    output_filename = 'output_audio.mp3'
    voice_name='voice_name'
    success = synthesize_speech(text, voice_name=voice_name, filename=output_filename, subscription_key=subscription_key, region=region)

    if success:
        return send_file(output_filename, as_attachment=True)
    else:
        return "Text-to-Speech synthesis failed"
    
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
