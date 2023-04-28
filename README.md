## Tutorial

[https://www.youtube.com/watch?v=1xtrIEwY_zY&t=3317s](https://www.youtube.com/watch?v=1xtrIEwY_zY&t=3317s)

## Running

`uvicorn main:app --reload`

this starts the application in development mode (refreshes on code changes)

## Api

http://localhost:8000/

```json
{
  "message": "Server running on port: 8000"
}
```

below endpoint gives the top 5 recommendations based on movie name or title

http://localhost:8000/search?movie=Avatar

```json
[
  "Aliens vs Predator: Requiem",
  "Aliens",
  "Falcon Rising",
  "Independence Day",
  "Titan A.E."
]
```

below endpoint gives the list of movie names for which we can get the recommendations

http://localhost:8000/movies

```json
[
  "Avatar",
  "Pirates of the Caribbean: At World's End",
  "Spectre",
  "The Dark Knight Rises",
  "John Carter",
  "Spider-Man 3",
  "Tangled",
  "Avengers: Age of Ultron",
  "Harry Potter and the Half-Blood Prince",
  "Batman v Superman: Dawn of Justice",
  "Superman Returns",
  "Quantum of Solace",
  "Pirates of the Caribbean: Dead Man's Chest",
  "The Lone Ranger",
  "Man of Steel"
]
```
