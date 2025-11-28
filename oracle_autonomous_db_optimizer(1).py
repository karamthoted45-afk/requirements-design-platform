
import time
import pandas as pd

MOCK_DATA = [{"id": i, "name": f"Employee {i}"} for i in range(1, 500)]

def mock_query_execution(query):
    start = time.time()
    if "500" in query:
        time.sleep(0.4)
        rows = MOCK_DATA[:500]
    elif "1000" in query:
        time.sleep(1.5)
        rows = MOCK_DATA
    else:
        time.sleep(0.1)
        rows = MOCK_DATA[:100]
    end = time.time()
    return (end - start), rows

def analyze_query_performance(query):
    exec_time, rows = mock_query_execution(query)
    print(f"Execution Time: {exec_time:.4f}s")
    print(f"Rows Returned: {len(rows)}")
    return exec_time

def suggest_optimization(exec_time):
    if exec_time > 2:
        return "Add indexes or partition tables."
    elif exec_time > 1:
        return "Optimize joins and filters."
    else:
        return "Query is optimized."

if __name__ == "__main__":
    query = "SELECT * FROM employees FETCH FIRST 500 ROWS ONLY"
    exec_time = analyze_query_performance(query)
    print(suggest_optimization(exec_time))
