# Module 1 Assignments — README

This folder contains the assignment notebooks for Module 1. Each notebook is organized into clearly labeled markdown + code cell pairs, one per task.

## How to run

1. Open the target assignment notebook (e.g. `Assignment2.ipynb`) in VS Code or Jupyter.
2. Run the cells from top to bottom in order (`Run All`), or run each task's cell individually — tasks are independent of each other.
3. Some cells use `input()` and will prompt for values in the notebook's input box; enter a numeric value when asked.

## Assignment2.ipynb — Control Flow (Conditionals and Loops)

- **Task 1 — Discount Rules (if/elif/else):** Prompts for `order_amount` via `input()`, applies tiered discount rules, then adds 5% tax and prints subtotal/tax/final total. Run the cell and enter a numeric amount when prompted.
- **Task 2 — Process Multiple Orders (for loop):** Uses a fixed list of order amounts and an explicit `for` loop to apply the same discount rules, printing a summary table (`order_amount -> discount% -> final_amount`), total revenue, and count of discounted orders. No input required — just run the cell.
- **Task 3 — User Menu (while loop + break/continue):** Runs an interactive menu loop. Enter `1` to add an order amount, `2` to view all orders with discounts applied, or `q` to quit.
- **Task 4 — Data Validation (for + continue + break):** Iterates over a fixed list of sales values, skipping `0` (no-sale day) with `continue` and stopping on `-1` (corrupted data) with `break`, printing the running and final totals. No input required — just run the cell.

## Notes

- All solutions in `Assignment2.ipynb` use only conditionals and loops (no functions, classes, or file I/O), per the assignment restrictions.
