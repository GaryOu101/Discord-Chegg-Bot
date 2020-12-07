# Discord-Chegg-Bot
* In this project, I created a Discord bot that takes a Chegg URL and generates a PDF file containing the contents of the given URL. The purpose of this bot is to allow the owner to share his/her Chegg subscription, in an automated fashion, with others who do not have a subscription. The bot opens the link in a web browser and utilizes pynput to simulate the key presses necessary to print the page as a PDF. The bot then uploads the PDF to the Discord channel where the request was made.

### Tools
* [discord.py](https://pypi.org/project/discord.py/)
* [Discord API](https://discord.com/developers/docs/intro)
* [pynput](https://pypi.org/project/pynput/)

### Input/Output
* Example of what a user would type:  .chegg <chegg-link>
  ![botinput](https://user-images.githubusercontent.com/42448439/101305996-af748c00-37f8-11eb-9158-41699c8157dc.png)
* PDF file the user receives:
  ![cheggbotoutput](https://user-images.githubusercontent.com/42448439/101307125-9a4d2c80-37fb-11eb-99c1-92b1df0b0498.PNG)
  
  
  ### Requirements to operate
  * Version of Python 3.6 (other versions may not work)
  * Discord API token
  * Access to a Chegg account
  
  ### Ending thoughts
 * Through this project, I learned how to access an API and utilize frameworks to perform specific tasks in my bot. While the bot may not operate 24/7 and requires the attention of my PC, I have gained insight into the process of problem solving and theorizing ideas of how my bot could operate. Additionally, since it was my first time programming in Python, I've learned many of the similarities and differences between Python and my main programming language of C++.
