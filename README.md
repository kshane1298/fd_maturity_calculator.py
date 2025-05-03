Thought for a second


Here’s a simple, non-technical guide to get the calculator running on your machine:

---

## 1. Install Python

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the big yellow button (“Download Python 3.x.x”).
3. Run the installer – **make sure** you check the box that says **“Add Python to PATH”** before you click “Install.”

---

## 2. Save the Script to a File

1. Open a plain-text editor:

   * **Windows:** Notepad
   * **macOS:** TextEdit (in plain-text mode)
   * **Linux:** gedit, nano, or any editor
2. Copy the entire code from our canvas (the `import math…` through `main()`) and paste it into the editor.
3. Save the file as **`fd_maturity_calculator.py`** on your Desktop (or any folder you’ll remember).

---

## 3. Open Your Terminal / Command Prompt

* **Windows:** Press `Win + R`, type `cmd`, hit Enter.
* **macOS:** Open “Terminal” from Spotlight (⌘+Space → type “Terminal”).
* **Linux:** Open “Terminal” from your Applications menu.

---

## 4. Navigate to the File’s Folder

In the terminal window, you need to “go” to where you saved the script. For example, if you saved it on your Desktop:

```bash
# Windows
cd %USERPROFILE%\Desktop

# macOS / Linux
cd ~/Desktop
```

Press Enter after you type that.

---

## 5. Run the Calculator with Your Numbers

The script takes four inputs:

* **`-P`** your principal (deposit) amount
* **`-R`** the annual rate in percent
* **`-T`** time in years
* **`-n`** compounding frequency per year (1 for yearly, 4 quarterly, 12 monthly, etc.)

Here’s an example command:

```bash
python fd_maturity_calculator.py -P 10000 -R 5.5 -T 3 -n 4
```

* This means:

  * You deposit ₹10,000
  * at 5.5% per year
  * for 3 years
  * compounded quarterly (4 times a year)

After you press Enter, you’ll see the maturity amount and total interest printed right below.

---

### Quick Recap

1. **Install** Python
2. **Save** the code as `fd_maturity_calculator.py`
3. **Open** Terminal/Command Prompt
4. **`cd`** into the folder where you saved the file
5. **Run** it with:

   ```bash
   python fd_maturity_calculator.py -P <your_deposit> -R <rate_%> -T <years> -n <frequency>
   ```

Feel free to ask if any step is unclear!
