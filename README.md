# Rotate Linked Lists

This repository is part of the problem set and class activity for Linked Lists in Unit 4.

## Learning Goals 
- Practice traversing a Linked List
- Practice writing functions that manipulate a Linked List

  
## One-Time Activity Setup

Follow these directions once, at the beginning of the activity:


1. Navigate to the folder where you wish to save activities. This could be your `projects` folder, or you may want to create a new folder for all of your activities.

   If you followed Ada's recommended file system structure, you can navigate to your projects folder with the following command:

   ```bash
   $ cd ~/Developer/projects
   ```

   Or, if you want to create a new folder for all of your activities:

   ```bash
   $ cd ~/Developer
   $ mkdir activities
   $ cd activities
   ```

   If you've already created an activities directory, you can navigate to it with the following command:

   ```bash
   $ cd ~/Developer/activities
   ```

2. In Github click on the "Fork" button to fork the repository to your Github account.  This will make a copy of the activity in your Github account. 

3. "Clone" the activity into your working folder. This command makes a new folder named for the activity repository, and then puts the activity into this new folder.

   ```bash
   $ git clone <clone_url_for_the_activity>
   ```

   The `<>` syntax indicates a placeholder. You should replace `<clone_url_for_the_activity>` with the actual URL you'd use to clone this repository. If you click the green "Code" button on the GitHub page for this repository, you'll see a URL that you can copy to your clipboard.
 
   Use `ls` to confirm there's a new activity folder

4. Move your location into this activity folder

   ```bash
   $ cd <repository_directory>
   ```

   The `<repository_directory>` placeholder should be replaced with the name of the activity folder. If you're not sure what the folder is named, remember that you can use `ls` to list the contents of your current location.

5. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

6. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:
   
   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this activity with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

   Not all activities will have dependencies, but there will still be an included `requirements.txt` file.

Summary of one-time activity setup:
- [ ] Fork the activity repository
- [ ] `cd` into your working folder, such as your `projects` or `activities` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the folder for the activity
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Activity Development Workflow

1. When working on this activity, always ensure that your virtual environment is activated:

   ```bash
   $ source venv/bin/activate
   ```

2. If you want to work on another project from the same terminal window, you should deactivate the virtual environment when you are done working on the activity:

   ```bash
   $ deactivate
   ```

## Part 1

### Live Code - Rotating A Linked List 
Implement a function which rotates a singly linked list `k` times.

One rotation can be performed by taking the last node in the linked list and placing it as the head of the list. For this problem, consider the linked list to be singly linked.

### Example 1:
Input: *list = 5 -> 3 -> 4 -> 2, k = 2*

Output: *4 -> 2 -> 5 -> 3*

*Explanation*: The last value in the linked list, 2 was placed at the head of the list, then the value 4 was placed as the head of the list. After 2 rotations, the list will look like the expected output.

### Example 2:
Input: *list = 22 -> 100 -> 55 -> 94 -> 7, k = 8*

Output: *55 -> 94 -> 7 -> 22 -> 100*

### Example 3:
Input: *list = 3 -> 5 -> 7, k = 0*

Output: *3 -> 5 -> 7*


We have provided the `ListNode` class as well as the `stringify_list` and `is_equal` functions that will be used for testing purposes. Please DO NOT MODIFY them.

*Note*: For the live code, we will only be implementing the `rotate_list` function. the `rotate_list` function will use the `add_first` and `get_last_two_nodes` helper functions but those will not be implemented until Part 2: the classroom activity.

## Part 2

## Classroom Activity - Implement Helper Functions

We have provided starter code for the functions `add_first` and `get_last_two_nodes` which are used within the `rotate_list`. Your job is to use what you know about Linked Lists to complete these functions. A description of what each function should do can be found below and in the respective docstrings:

- `add_first`: This function takes in two nodes, the old_head node will be the node that was previously the head of the list, the `node` will be the node that will replace the old head of the list.
  
    - Parameters:
        - `old_head (ListNode)`: old head of the linked list
    
        - `node (ListNode)`: node to be set to the new head of the list
  
    - Returns:
        - `ListNode`: the new head of the list

- `get_last_two_nodes`: This function accepts the head of a linked list and returns the last two nodes in the linked list.

    - Parameters:
      - `head (ListNode)`: the head of the linked list from which we want to find the last two nodes

    -  Returns:
       - `tuple (ListNode, ListNode)`: the last two nodes of the linked list, in the order in which they appear in the list

There are individual tests for these two functions. Once they are passing, the tests for the `rotate_list` function should pass as well!
 
## Running Tests
Use the tests provided in the `test_rotate_linked_list.py` file to verify that your code is working correctly. You can verify the tests are working in one of two ways:

1. Run `pytest` in the terminal (make sure you are in the venv!)
2. Set up the testing environment in the VSCode Testing Pane
   1. Click on the beaker icon and click `Configure Python Tests`
   2. Select `pytest` from the list that appears
   3. Select `tests` from the new list that appears.
3. Verify the tests show up in the Testing Pane.
4. Run the tests to make sure they are all passing!
