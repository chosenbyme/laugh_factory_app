
# Laugh Factory Application

An application where you can view funny memes. You can sign up for an account
to be able to share your own memes, you can also comment and react to memes you think are funny.


## Technology 
Python3

Flask

SQLAlchemy
## Installation



```bash
  python3 -m venv venv 
  source venv/bin/activate 
  pip install -r requirements.txt    

  flask run --reload
```
    
## Routes

|Method	     |Path	            |Purpose|
|------------|------------------|-----------------------------------------------------------|
|GET	     |/	                |The Main page|
|GET	     |/user:name	    |The Main page(logged in)|
|POST	     |/signup	        |sign up page(form)|
|GET	     |/log in	        |log in page(form)|
|POST	     |/upload	        |Upload a new meme|
|GET	     |/meme/:id	        |Show one meme in details|
|PUT	     |/meme/:id/edit	|Edit one meme's attributes|
|PUT	     |/meme/:id	        |Comment on a meme|
|DELETE	     |/meme/:id	        |Delete a meme|



## Authors

- [Ivelisse Mandato](https://www.github.com/imandato)
- [Yekai Guan](https://www.github.com/chosenbyme)
- [Anibal Hugo](https://www.github.com/ahugo93)


## Feedback

If you have any feedback, please reach out to us!

