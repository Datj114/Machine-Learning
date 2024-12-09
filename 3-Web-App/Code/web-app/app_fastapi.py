# import numpy as np
# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# import pickle

# app = FastAPI()
# model = pickle.load(open('/media/dat/code/ML-For-Beginners/3-Web-App/Code/web-app/ufo_model.pkl', 'rb'))

# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/predict")
# async def predict(request: Request, seconds: int = Form(...), latitude: float = Form(...), longitude: float = Form(...)):
#     int_features = [seconds, latitude, longitude]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     output = prediction[0]
#     countries = ["Australia", "Canada", "Germany", "UK", "US"]

#     return templates.TemplateResponse(
#         "index.html", {"request": request, "prediction_text": f"Likely country: {countries[output]}"}
#     )

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app)
