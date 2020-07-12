import json
import requests
data = '''
{
	"full_name": "Eglardo Fabricio Alves dos Santos",
	"email": "eglardoalves@gmail.com",
	"mobile_phone": "+55 (83) 999-567-056",
	"age": 35,
	"home_address": "440 José Lins do Rêgo Street, Campina Grande City PB",
	"start_date": 1573077739,
	"opportunity_tag": "dev_intern_200",
	"past_jobs_experience": "I worked as a sailor on fishing vessels. Took care of deck maintenance and cleaning for 3 years on 7 seas.",
	"degrees": [{
		"institution_name": "Universidade Federal de Campina Grande",
		"degree_name": "Electronic Engineer",
		"begin_date": 1139220000,
		"end_date": 1307700000000
	},{
		"institution_name": "Universidade Estácio de Sá",
		"degree_name": "Post graduate MBA Software Engineer",
		"begin_date": 1562580000000,
		"end_date": 1597226400000
	}],
	"programming_skills": ["python", "java", "C", "C++", "C#","Assembly","VHDL"],
	"database_skills": ["mysql", "postgresql"],
	"hobbies": ["sailing", "soccer play", "reading", "running"],
	"why": "I would like work with new technology for upgrade and join software process as Machine Learning, inteligence artificial, IoT, as well as helping connect data from field and development one better results and build one good Agrotech, to apply with software, hardware and renewable energy can give return better profits and gains in harvests", 
	"git_url_repositories": "https://github.com/eglardo"
        }
'''
resume_data = json.loads(data)
resume_data

r = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume')
print(r.status_code)
type(resume_data)
print(resume_data.keys())
print(r.content)

url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'
x = requests.post(url, json = data)
print(r.status_code)
print(x.content)
