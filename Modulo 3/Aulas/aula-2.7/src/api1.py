from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
count =0


@app.get("/", response_class=HTMLResponse)
async def root():
  global count
  count = count +1 
  return f""""
      <html>
        <head>
          <title>My FastApi</title>
        </head>

        <body style="background: radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(64, 64, 64) 90.2%);">
          <div style="text-align: center;line-height: 200px;color: rgb(0, 201, 0);">
            <h1>XP Educação | Aprenda com quem faz</h1>
          </div>
          <div style="text-align: center;line-height: 200px;color: rgb(0, 201, 0);">
            <h1>count: {count}</h1>
          </div>
        </body>
      </html>  
  """

@app.get("/healthz")
async def health():
  return {
    "message": "ok!"
  }