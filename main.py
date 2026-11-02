from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notes = []


class NoteCreate(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    new_note = {"id": len(notes) + 1, "title": note.title, "content": note.content}
    notes.append(new_note)
    return new_note


@app.get("/notes")
def list_notes():
    return notes

@app.delete("/delete")
def delete_notes():
    