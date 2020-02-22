from flask import Flask, render_template, request, redirect, url_for
import yweather
import tweepy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'canyoukeepasecret'
client = yweather.Client()

auth = tweepy.OAuthHandler("your_API_KEY, your_API_secret_key")
auth.set_access_token("your acces_token_key, your_access_token_secret")
api = tweepy.API(auth)

@app.route('/')
def index():
    location = request.args.get("location")
    trends = None
    if location:
        loc_id = client.fetch_woeid(str(location))
        trends = api.trends_place(int(loc_id))
        return render_template('index.html',trends=trends)
    else:
        location = 1
        trends = api.trends_place(location)
        return render_template('index.html',trends=trends)

if __name__ == "__main__":
    app.run(debug=True)
