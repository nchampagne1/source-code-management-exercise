Here are the instructions you can copy and paste into both the `README.md` file in the repository and the email you send to the class.

---

# Source Code Management Exercise

## Objective
In this exercise, you will demonstrate your understanding of Git and GitHub by forking this repository, adding a Python function, and submitting a pull request. You will write a function to calculate the Greatest Common Divisor (GCD) of two integers using the **Euclidean algorithm** and follow a precise workflow to manage your source code.

## Instructions

### Step 1: Fork the Repository
- Fork this repository to your own GitHub account by clicking the **Fork** button in the upper right corner. *Note* if you change the name of your repository, then you will need to use your repo name instead of `source-code-management-exercise` when following the examples below.

### Step 2: Clone Your Fork
- Clone the forked repository to your local machine. Open your terminal and run the following command:
  ```bash
  git clone https://github.com/<your-github-username>/source-code-management-exercise.git
  ```

### Step 3: Create a New Branch
- Create a new branch to work on your feature. Name your branch `<ucid>-gcd-feature` where <ucid> is your student ucid (`wfm8`). Example commands:
  ```bash
  cd source-code-management-exercise
  git checkout -b <ucid>-gcd-feature
  ```

### Step 4: Create Your Submission File
- Inside the `students_submissions/` directory, create a new Python file named `gcd_<GitHubUsername>.py`. Replace `<GitHubUsername>` with your actual GitHub username.
  - Example: If your GitHub username is `johndoe`, name your file `gcd_johndoe.py`.

### Step 5: Implement the `gcd` Function
- In your `gcd_<GitHubUsername>.py` file, a greatest common divisor function. Use this exact function signature: `def gcd(a: int, b: int) -> int:`. DO NOT USE LOOPS in your function. Be sure to consider edge cases, like prime numbers, negative numbers, etc.
  ```python
  def gcd(a: int, b: int) -> int:
      """
      Calculate the greatest common divisor (GCD) of two integers a and b
      using the Euclidean algorithm.
      """
      # Implement your solution here
      pass
  ```

- Test your function with some basic test cases inside your file. You can use `print` statements to verify your implementation.

Example:
```python
def gcd(a: int, b: int) -> int:
    # This uses a loop, so DO NOT COPY AND PASTE this example
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
```

### Step 6: Commit Your Changes
- Once your function is implemented, stage and commit your changes:
  ```bash
  git add students_submissions/gcd_<GitHubUsername>.py
  git commit -m "Implemented GCD function"
  ```

### Step 7: Push the Branch to GitHub
- Push your changes to the `gcd-feature` branch in your forked repository:
  ```bash
  git push origin gcd-feature
  ```

### Step 8: Create a Pull Request
- Go to your forked repository on GitHub and click the **Compare & pull request** button.
- Make sure to select your `gcd-feature` branch as the source and the original repository’s `main` branch as the destination.
- Submit the pull request.

---

## Naming Conventions
To ensure your submission is automatically checked, you must follow these naming conventions:
1. Your Python file must be placed in the `students_submissions/` directory.
2. The file must be named `gcd_<GitHubUsername>.py`, where `<GitHubUsername>` is your actual GitHub username (e.g., `gcd_johndoe.py`).
3. Your file must contain a function named `gcd(a: int, b: int) -> int`.

If you do not follow these conventions, your submission will not be automatically tested, and you may be asked to resubmit.

---

## Submission Deadline
- Your pull request must be submitted by [INSERT DEADLINE DATE AND TIME].

---

### Notes:
- If you encounter any issues, feel free to reach out for help.
- Remember to test your function with a variety of inputs to ensure it works correctly.
- Follow the naming conventions carefully to avoid any issues with the automatic testing.

---
