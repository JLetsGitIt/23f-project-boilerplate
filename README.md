# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## Overview of Project
With the closing of traditional brick and mortar retail toy stores and the rising prevalence of digital forms of entertainment, physical toy sales have undergone a massive drop in recent years. Our project, "Kiddo Creations," is an online initiative aimed at addressing this issue by reviving the joy of a physical experience to nurture the imagination of the digital generation, primarily targeted at children aged 5-12 years old. This project is a toy sale endeavor that seeks to provide high-quality, engaging, and educational toys that chain corporations like Target cannot provide. These toys are personalized to enhance the experience and designed to capture the attention of children who spend excessive time online, through reawakening their innate curiosity, creativity, and desire for hands-on experiences. 
