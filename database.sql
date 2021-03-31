CREATE TABLE "games" (
    "id" SERIAL PRIMARY KEY,
    "game" VARCHAR (80) UNIQUE NOT NULL,
    "developer" VARCHAR (1000) NOT NULL
);
