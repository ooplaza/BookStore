# The key point is that with Docker we don’t need to be in a local virtual environment anymore.
# Docker is our virtual environment…and our database and more if desired. The Docker host
# essentially replaces our local operating system and within it we can run multiple containers,
# such as for our web app and for our database, which can all be isolated and run separately.


# Base Image
FROM python:3.11-bullseye

# Set Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Working Directory
WORKDIR /code

# Copying the requirements into the docker root directory
COPY ./requirements.txt .

# Execute the requirements
RUN pip install -r requirements.txt

# Copy Project
COPY . .