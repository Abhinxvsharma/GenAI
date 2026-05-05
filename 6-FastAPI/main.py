from fastapi import FastAPI
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware




app=FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], 
                   allow_methods=["*"], 
                   allow_headers=["*"])


class Item(BaseModel):
    id:int
    name:str
    description:str
    price:float


dummy_database = [Item(id=1, name="Item 1", description="This is item 1", price=10.0),
                    Item(id=2, name="Item 2", description="This is item 2", price=20),
                    Item(id=3, name="Item 3", description="This is item 3", price=30)]

@app.get("/")
def greet():
    return {"message": "My API is working!"}


@app.get("/items")
def get_items():
    return dummy_database


@app.post("/item_data")
def create_item(item: Item):
    dummy_database.append(item)
    return {"message": "The item has been added to the database successfully!"}


@app.get("/item_data/{item_id}")
def get_item(item_id: int):
    for item in dummy_database:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}


@app.put("/item_data/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(dummy_database):
        if item.id == item_id:
            dummy_database[index] = updated_item
            return {"message": "The item has been updated successfully!"}
    return {"message": "Item not found"}


@app.delete("/item_data/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(dummy_database):
        if item.id == item_id:
            del dummy_database[index]
            return {"message": "The item has been deleted successfully!"}
    return {"message": "Item not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)


# python main.py     ....se run the server and then open http:// 
# uvicorn main:app --reload   .......to run the server with auto-reload on code changes.    