# Battle of the knights

To run the code:

* Clone the repo and cd into the top level directory
* Add a file at the top level with a list of moves, see for example: 'moves.txt'
* Run the following command in the terminal :

  `python3 runner.py 'moves.txt'`

  Or

  `python3 runner.py 'moves.txt' 'yes'`

> _'yes' is optional, it will export the output to a new file_

---

To run the tests:

* You need to install pytest (if you don't have pip you might need to install
  that first):

  `pip install pytest`

  Or from the same level directory as the requirements file:

  `pip install -r requirements.txt`

* Run the following command at the top level of the directory:

  `pytest`
