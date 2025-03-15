Test Management Module

This Odoo module is designed to manage test cases, test runs, test steps, and bugs in a structured and efficient manner. It provides a comprehensive solution for quality assurance teams to plan, execute, and track testing activities. Features

    Test Case Management

    Test Case Lifecycle Management:

     Track test cases through their lifecycle with states: Draft, Under Review, Approved, Running,  and Executed.

     Automatically log timestamps for key events (e.g., creation date, review date, execution date).

State Transitions:

 To Review: Transition a test case from Draft to Under Review.

 Approved: Transition a test case from Under Review to Approved.

 Run: Transition a test case from Approved to Running.

 Set to Draft: Revert a test case from Under Review to Draft.

 Re-run: Re-run a test case from Executed to Running.

Priority and Severity:

 Set the Priority of a test case (Low, Medium, High, Critical).

 Track the State of a test case (e.g., Draft, Approved, Running).

Advanced Filters and Grouping:

 Filter test cases by Priority, State, Assignee, and Project.

 Group test cases by State, Project, Component, and Priority.

Kanban View:

 Visualize test cases in a Kanban board grouped by state.

 Use color-coded progress bars to track test case status.

Graph and Pivot Views:

 Analyze test case data using graphs (e.g., test cases by state) and pivot tables (e.g., test cases by project and state).

Test Run Management

Test Run Lifecycle Management:

 Track test runs through their lifecycle with states: Draft, In Progress, and Completed.

 Automatically log timestamps for key events (e.g., start date, end date).

State Transitions:

 Start Run: Transition a test run from Draft to In Progress.

 Complete: Transition a test run from In Progress to Completed and update the test case state to Executed.

Test Steps Execution:

 Execute test steps and log the actual results.

 Mark test steps as Passed, Failed, or Blocked.

 Report bugs directly from failed or blocked test steps.

Bug Tracking:

 Track bugs associated with a test run.

 View a list of related bugs from the test run form.

Advanced Filters and Grouping:

 Filter test runs by State, Status, Project, and Component.

 Group test runs by Test Case, State, Project, Component, and Result.

Graph and Pivot Views:

 Analyze test run data using graphs (e.g., test runs by status) and pivot tables (e.g., test runs by project and component).

Bug Tracking

Bug Lifecycle Management:

 Track bugs through their lifecycle with states: New, Confirmed, In Progress, Fixed, Retesting, Re-opened, and Closed.

 Automatically log timestamps for key events (e.g., reported date, fix start date, fix end date).

State Transitions:

 Confirm: Transition a bug from New to Confirmed.

 Start Fixing: Transition a bug from Confirmed or Re-opened to In Progress.

 Resolved: Transition a bug from In Progress to Fixed.

 Reopen: Reopen a bug from Fixed to Confirmed using a wizard.

 Closed: Transition a bug from Fixed to Closed.

Automated Activities:

 Schedule activities for bug assignment, reopening, fixing, and closing.

 Notify users when a bug is assigned, reopened, fixed, or closed.

Time Tracking:

 Log Fix Start Date and Fix End Date when a bug is fixed.

 Track the time taken to resolve a bug.

Advanced Filters and Grouping:

 Filter bugs by Severity, Priority, State, Assignee, and Project.

 Group bugs by State, Project, Component, Test Case, Priority, and Severity.

Kanban View:

 Visualize bugs in a Kanban board grouped by state.

 Use color-coded progress bars to track bug status.

Graph and Pivot Views:

 Analyze bug data using graphs (e.g., bugs by severity) and pivot tables (e.g., bugs by project and state).

    Project Integration: Each project now displays the number of associated bugs and test cases.

    These counts are automatically computed and updated in real-time.

Quick Access to Bugs and Test Cases:

 From the project form, you can directly access the list of bugs and test cases associated with the project.

 Use the View Bugs and View Test Cases buttons to open filtered lists of bugs and test cases.

Installation

    Prerequisites

    Odoo 17.0.

    Installation Steps

    Download the module to your Odoo addons directory

    Restart the Odoo server.

    Go to the Odoo Apps menu and search for Test Management Module.

    Click Install.

Configuration

    Access Rights

    Assign the appropriate access rights to users:

     QA Engineer: Full access to test cases, test runs, and bugs.

     Developer: Access to bugs.

Support

For any issues or questions, please contact:

Email: applyit4@gmail.com
