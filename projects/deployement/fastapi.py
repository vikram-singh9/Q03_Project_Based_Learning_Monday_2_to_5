from fastapi import FastAPI


app = FastAPI()


def get_items():
    return {"items": [{"name": "Foo"}, {"name": "Bar"}]}