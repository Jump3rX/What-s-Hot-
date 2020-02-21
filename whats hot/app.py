from flask import Flask, render_template, request, redirect, url_for
import yweather
import tweepy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'canyoukeepasecret'
client = yweather.Client()

auth = tweepy.OAuthHandler("FqyooQamrl1rf6POvlilOqcY5","UryLa3N4bmEVFmRWVO09Aks6YoNFgxUojUafJZVFHkm3K05tOF")
auth.set_access_token("2745497499-isFWOMENSyndVn1lLDQm4bZO9om0NqzUjg6n4z5","jU5BmG5sWAg8asXxSJQ8vLm0z8ClVjjhFk4MoCxUaO6eT")
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