# Onmyoji_Automation
# About me (UPDATED Jan 2023)
 - Wenbo Zhang ([Wenbo Zhang]())

 I'm a 3rd year student currently studying computer science in Ontario Tech University. I'm interested in Computer Vision, Machine Learning, AI and NLP. Currently I'm a Self-Made Web Application developer and Site-Manager (Webpage current under development and not available now).



 # Introduction

 ## Reasons for developing this script

 After a semester of computer vision torturing, I suddenly started to find computer vision actually pretty interesting, and this time it was the "化四季" activity. So I thought, Why don't I develop a script that can automate the completion of the copy to get the scrolls? So I can easily to get top 10 position on the tanking to get 60 pieces of "Shiki".

 For people like me who can't summon a new character every time, I always want to be able to spell out a complete new character during the event. But this stuff requires basically playing the game 24 hours a day, and as a third-year student, I barely have time to play the game. In the introduction also said, in this script used the knowledge of computer vision, on this course, Lab writing a week can not finish writing, to the last Lab even wrote until 4:00 am can not finish writing, where I have time to play games? QAQ

 ## Technology used in this script

 Computer Vishion, Numpy, Mathplotlib.pyplot, Python

## Running Environment
 
### Tested good on:

#### MacOS (Apple silicon):

For Macos, I haven't tested about mouse moving part, and "win32api" library also not working on Macos. I only use Mac environment for developing the computer vision part and optimizing algorithm.

- Macos Monterey 12.6, Conda python 3.7.13 environment. 10-cores M1 Pro chip with 32GB RAM

#### Windows (AMD-64)

- Windows 10 21H2, Conda Python 3.9.13 environment. Intel i7-8550u, 16GB RAM, NVIDIA MX150

# Analisis of Technology Used
In this section, I will detail the idea of developing the script. Some of the steps might be useless and I'll keep improving it.
## Part 1: Challenge button detection

### Button template processes
Firstly, I took a screenshot of the waiting interface for two peolpe as a team, then crop the challenge button.
![](https://github.com/Falanan/Onmyoji_Automation/blob/main/Onmyoji_Automation_Script/pics/03-T.jpg?raw=true)

This picture will be used as a template later in the whole program. The shape of the cropped template image is (214, 187, 3).

Then reshape the image to 128 x 128 as showen below.

<img src = "https://github.com/Falanan/Onmyoji_Automation/blob/main/readme_file_pics/128_cb.png?raw=true" width="128px">

The reason resize the image to 128 x 128 size is later in the process, to make sure the dector work well with any window resolution, so it need to generate down sampling and gaussian pyramids for the template. To generate the gaussian pyramid, squared image is needed, so resize the image to 128 x 128 at the very begining to avoid other problems.

<img src = "https://github.com/Falanan/Onmyoji_Automation/blob/main/readme_file_pics/ds.png">

Down sampled images for button template.

Then generate gaussian pyramids for each different resolution templates. For demonstration purpose, I only make the gaussian pyramid for 128 x 128 resolution.

<img src="https://github.com/Falanan/Onmyoji_Automation/blob/main/readme_file_pics/gp_128.png?raw=true">

### Image processes

Image procedures are pretty the same as tamplate processing.

Firstly, generate gaussian pyramid for the image, as shown below:

<img src="https://github.com/Falanan/Onmyoji_Automation/blob/main/readme_file_pics/gpI.png?raw=true">

But some of them are useless, such as most of the images of second row.