## AMC/AIME Problem Set Creator
This program randomly extracts AMC/AIME questions from AOPS and creates a PDF worksheet. 

## Question Sample Rules:
AMC questions are sampled between years 2015-2023 inclusive and AIME questions are sampled between years 2005-2023 inclusive. 

AMC questions are sampled according to a normal distribution centered at question no.18 with standard deviation 3. 

AIME questions are sampled according to a normal distribution centered at question no.6 with standard deviation 4.

If you want to change the difficulty setting, you can change the parameters in the code.

## Deployment
This app is also deployed on [Huggingface Spaces](https://huggingface.co/spaces/ymcmy/AMC_AIME_Random_Problem_Set_Generator). 

Run with local python environment:
```sh
pip install -r requirements.txt
python gen_pdf.py 5 # generate worsheet with 5 problems
```

Run with docker:
```docker
docker run -it -p 7860:7860 --platform=linux/amd64 \
	registry.hf.space/ymcmy-amc-aime-random-problem-set-generator:latest python app.py
```