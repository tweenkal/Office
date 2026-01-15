company = {
    "robert_downey": {
        "designation": "project_manager",
        "TL": {
            "mark": {"designation": "TL", "experience": 8,
                     "employee": {
                         "leonardo": {"designation": "junior_developer",
                                      "experience": 1},
                         "Alexandra": {"designation": "junior_developer",
                                       "experience": 1}
                     }
                     },

            "samuel": {"designation": "TL", "experience": 8},
            "paul": {"designation": "TL", "experience": 8,
                     "employee": {
                         "fergal": {"designation": "senior_developer",
                                    "experience": 4.5}
                     }
                     },
            "tom": {"designation": "TL", "experience": 8,
                    "employee": {
                        "jerry": {"designation": "senior_developer",
                                  "experience": 1.5},
                        "john": {"designation": "senior_developer",
                                 "experience": 1.6}
                    }
                    }
        }
    },

    "anne_hathaway": {
        "designation": "project_manager",
        "TL": {
            "chris": {"designation": "TL", "experience": 5,
                      "employee": {
                          "james": {
                              "designation": "TL", "experience": None,
                              "employee": {
                                  "jennifer": {
                                      "designation": "senior_developer",
                                      "experience": 3.8},
                                  "scott": {"designation": "senior_developer",
                                            "experience": 3.8},
                                  "sophie": {"designation": "senior_developer",
                                             "experience": 3.8}
                              }
                          }
                      }
                      },

            "pratt": {"designation": "TL", "experience": 5},
            "emma": {"designation": "TL", "experience": 5},
            "will": {"designation": "TL", "experience": 5,
                     "employee": {
                         "edge": {"designation": "senior_developer",
                                  "experience": 3},
                         "ryan": {"designation": "senior_developer",
                                  "experience": 3.5}
                     }
                     },
            "smith": {"designation": "TL", "experience": 5,
                      "employee": {
                          "walker": {"designation": "senior_developer",
                                     "experience": 2.7},
                          "diana": {"designation": "senior_developer",
                                    "experience": 2.7}
                      }
                      }
        }
    }
}

# A.Display all employees' names for the given project manager name
print("1) Display all employees' names for the given project manager")
print("---------------------------------------------------------------")

pm_list = [
    input("Enter the first Project Manager name: ").strip(),
    input("Enter the second Project Manager name: ").strip()
]

for pm_name in pm_list:
    if pm_name not in company:
        print(f"Project Manager '{pm_name}' not found!")
        continue
    else:
        print(f"Project Manager: {pm_name}")
    pm_info = company[pm_name]

    for tl_name, tl_info in pm_info["TL"].items():
        print("TL:", tl_name)
        for emp_name, emp_info in tl_info.get("employee", {}).items():
            print("Employee:", emp_name)
            if emp_info.get("designation") == "TL":
                for sub_emp in emp_info.get("employee", {}):
                    print(" Employee under TL:", sub_emp)

# B.Display names of only those employees whose
# experience is more than 4 years.
print("\n2) Display names of only those employees whose"
      " experience is more than 4 years.")
print("-------------------------------------------------------------")

for pm_info in company.values():
    for tl_info in pm_info["TL"].values():
        for emp_name, emp_info in tl_info.get("employee", {}).items():
            if (emp_info.get("designation") != "TL"
                    and emp_info.get("experience", 0) > 4):
                print(emp_name)

            for nested_name, nested_info in \
                    emp_info.get("employee", {}).items():
                if nested_info.get("experience", 0) > 4:
                    print(nested_name)

# C.Update years of experience with 4.6 whose experience is
# greater than 3.5 and less than 4.5 years.
print("\n3))Update years of experience with 4.6 whose "
      "experience is greater than 3.5 and less than 4.5 years.")
print("----------------------------------------------------------")

for pm_name, pm_info in company.items():
    print(f"\nProject Manager: {pm_name}")

    for tl_name, tl_info in pm_info["TL"].items():
        if tl_info.get("experience") and 3.5 < tl_info["experience"] < 4.5:
            tl_info["experience"] = 4.6
        print(f"TL: {tl_name}, Experience: {tl_info.get('experience')}")

        for emp_name, emp_info in tl_info.get("employee", {}).items():
            if (emp_info.get("experience")
                    and 3.5 < emp_info["experience"] < 4.5):
                emp_info["experience"] = 4.6
            print(f"Employee: {emp_name}, "
                  f"Experience: {emp_info.get('experience')}")

            for nested_name, nested_info \
                    in emp_info.get("employee", {}).items():
                if (nested_info.get("experience")
                        and 3.5 < nested_info["experience"] < 4.5):
                    nested_info["experience"] = 4.6
                print(f"Nested Employee: {nested_name}, "
                      f"Experience: {nested_info.get('experience')}")

# D.Display TL with their year of experience, if has no
# experience then display N/A. Display all TLs with their
# experience (N/A if None)
print("\n4) TLs with their year of experience (N/A if missing)")
print("------------------------------------------------------")

for pm_name, pm_info in company.items():
    print(f"\nProject Manager: {pm_name}")

    for tl_name, tl_info in pm_info["TL"].items():
        if tl_info.get("experience") is not None:
            exp = tl_info["experience"]
        else:
            exp = "N/A"
        print(f"TL: {tl_name}, Experience: {exp}")

        if "employee" in tl_info:
            for emp_name, emp_info in tl_info["employee"].items():
                if emp_info.get("designation") == "TL":
                    if emp_info.get("experience") is not None:
                        exp_nested = emp_info["experience"]
                    else:
                        exp_nested = "N/A"
                    print(f" TL: {emp_name}, Experience: {exp_nested}")

# E.Smith left the company and all his members were assigned to Ryan
print("\n5))Smith left the company and all his members were assigned to Ryan")
print("--------------------------------------------------------")

anne_tl = company["anne_hathaway"]["TL"]

if "smith" in anne_tl:
    smith_employees = anne_tl["smith"].get("employee", {})
    print("\nEmployees being transferred from Smith to Ryan:")

    for emp_name, emp_info in smith_employees.items():
        print(f"{emp_name} -> {emp_info['experience']}")

    ryan_record = anne_tl["will"]["employee"]["ryan"]
    ryan_record.update(smith_employees)

    del anne_tl["smith"]
else:
    print("Smith is not present in Anne Hathaway's TL list!")

# F. Check company has any employee who has less than 2 years of experience
print("\n6))Check company has any employee who has less "
      "than 2 years of experience.")
print("-------------------------------------------------------------------")

for pm_name in company:
    for tl, tl_name in company[pm_name]["TL"].items():
        if tl_name.get("employee"):
            for key, value in tl_name["employee"].items():
                if (value.get("experience") is not None and
                        value.get("experience") < 2):
                    print(f"{key} -> {value.get('experience')}")

# G.Check whether Edge is TL or not if not make him TL.
print("\n7) Check whether Edge is TL or not — if not, make him TL.")
print("-------------------------------------------------------")

anne_tl = company["anne_hathaway"]["TL"]

edge_data = None
current_tl = None

for tl, tl_data in anne_tl.items():
    if "employee" in tl_data and "edge" in tl_data["employee"]:
        edge_data = tl_data["employee"]["edge"]
        current_tl = tl
        break

if "edge" not in anne_tl and edge_data is not None:
    del anne_tl[current_tl]["employee"]["edge"]

    anne_tl["edge"] = {
        "designation": "TL",
        "experience": edge_data.get("experience"),
        "employee": {}
    }

print("\nCurrent TLs under Anne Hathaway:")
for tl in anne_tl:
    print(tl)

if "edge" in company["anne_hathaway"]["TL"]:
    print("Edge promoted to TL ")
else:
    print("Edge is still an employee")
