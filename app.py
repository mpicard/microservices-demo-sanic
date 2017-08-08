import aiohttp

from sanic import Sanic
from sanic import response


app = Sanic()


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()


@app.route("/")
async def handle_request(request):
    user_url = 'https://api.github.com/users/mpicard'
    repo_url = 'https://api.github.com/users/mpicard/repos'

    async with aiohttp.ClientSession() as session:
        user_resp = await fetch(session, user_url)
        repo_resp = await fetch(session, repo_url)

        return response.json({
            'user': user_resp,
            'repos': repo_resp
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=2)
