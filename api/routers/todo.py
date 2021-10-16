from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models.todo import Author, Post, Category

app = APIRouter(
    prefix="/api/v1/serega/todo",
    tags=["Дела"]
    )

@app.post('/post')
async def create_author(first_name, last_name:str):
    guido = await Author.objects.create(first_name = first_name, last_name = last_name)
    return guido

@app.post('/post/variant2')
async def create_author2(guido :Author):
    return await guido.save()


@app.post('/create/post')
async def create_post(id_gnida:int):
    # gnida = await Author.objects.get(id = id_gnida)
    gnida = await Author.objects.get_or_none(id = id_gnida)
    post = await Post.objects.create(title="Hello, M2M", author=gnida)
    return post

@app.post('/add/post')
async def create_post(id_gnida:int,id_post):
    # gnida = await Author.objects.get(id = id_gnida)
    post = await Post.objects.get(id = id_post)
    # await post.save_related(author__first_name = 'gleb')
    gnida = await Author.objects.get_or_none(id = id_gnida)
    await post.update(author = gnida)
    return post



@app.get('/posts')
async def get_all():
    
    posts = await Post.objects.all()
    return posts

@app.post('/test')
async def test():
    guido = await Author.objects.create(first_name="Guido", last_name="Van Rossum")
    post = await Post.objects.create(title="Hello, M2M", author=guido)
    news = await Category.objects.create(name="News")
    return (guido,post,news)
    # data = {
    #     'post':post,
    #     'гниды':guido,
    #     'категории':news,
    # }
    # json_compatible_item_data = jsonable_encoder(data)
    # return JSONResponse(
    # status_code=200,
    # content=json_compatible_item_data
    # )
