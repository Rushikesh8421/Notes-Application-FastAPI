from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

notes = []
next_id = 1

class NoteCreate(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Hello World"}


# @app.post("/notes", status_code=201)
# def create_note(note: NoteCreate):
#     new_note = {"id": len(notes) + 1, "title": note.title, "content": note.content}
#     notes.append(new_note)
#     return new_note

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    global next_id
    new_note = {"id": next_id, "title": note.title, "content": note.content}
    next_id += 1
    notes.append(new_note)
    return new_note


@app.get("/notes")
def list_notes():
    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")



@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    for existing in notes:
        if existing["id"] == note_id:
            existing["title"] = note.title
            existing["content"] = note.content
            return existing
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for index, existing in enumerate(notes):
        if existing["id"] == note_id:
            notes.pop(index)
            return
    raise HTTPException(status_code=404, detail="Note not found")