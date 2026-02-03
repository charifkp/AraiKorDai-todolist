The system description below will be used as the
case study for developing our C4 diagrams.
ICT To Do List is a task management system for the ICT e learning environment. It supports
both a web based application and a mobile application. The purpose is to help students track
personal tasks and automatically track course work by syncing assignments and submission
status from MyCourses. A user can create tasks manually, and the system can also create tasks
from MyCourses assignments. The user can view tasks, update task details, delete tasks, and
mark tasks as done. Each task has a title, optional description, due date, status, and a source
flag that indicates whether the task is manual or imported from MyCourses. Imported tasks also
store the MyCourses assignment ID so the system can update the correct task during future
sync and avoid duplicates.
ITCS383 Software Construction and Evolution Updated: 26 Jan 2025
Lab week 4
The system has three primary user roles. Student is the main user who manages the task list,
views assignments, and tracks submission status. Instructor may use the system to view their
own teaching related tasks and monitor a high level view of assignment deadlines for the
courses they teach, but the instructor does not see student private tasks. System Administrator
manages system configuration, supports user accounts, and monitors sync health. The
administrator uses a separate admin interface provided by the web application or a dedicated
admin screen.
The system interacts with external systems. MyCourses is an external ICT e learning system
that owns course, assignment, and submission data. ICT To Do List must connect to MyCourses
to retrieve assignment lists and submission status for the authenticated user. MyCourses
exposes web services that return JSON payloads. The integration must support at least these
operations. Retrieve the list of active courses for the user. Retrieve assignments for a selected
course including assignment title, due date, and assignment ID. Retrieve submission status for
the user for each assignment, including submitted or not submitted and submission timestamp
when available. ICT To Do List treats MyCourses as the source of truth for imported
assignments and submission status.
ICT To Do List includes these internal containers and technology decisions. Web App is a
browser based user interface implemented as a single page application using React. Mobile
App is a cross platform mobile application implemented using Flutter so the same codebase can
support both iOS and Android. Web API is the backend service implemented using Python
FastAPI and exposes REST endpoints that accept and return JSON. Database is PostgreSQL,
used to store user profiles, tasks, sync settings, and sync history. MyCourses Connector is an
integration module running within the backend deployment, implemented as a separate service
module that calls MyCourses web services, parses JSON responses, and maps external data
into internal task records. All client requests from Web App and Mobile App go to the Web API
over HTTPS using JSON. The Web API reads and writes data in PostgreSQL using SQL
through an ORM such as SQLAlchemy. The Web API calls the MyCourses Connector over an
internal interface, such as a direct function call or an internal HTTP call if deployed as a
separate service. The MyCourses Connector communicates with MyCourses over HTTPS and
exchanges JSON with the MyCourses web services. Authentication uses university single sign
on when available. If MyCourses supports OAuth2 or OpenID Connect, ICT To Do List uses that
mechanism. If not, ICT To Do List uses its own account system and stores only the minimum
link needed to call MyCourses on behalf of the user.
The main user flows are as follows. A student signs in to ICT To Do List using the Web App or
Mobile App. After sign in, the client requests the current task list from the Web API. The student
can create a manual task by sending task details to the Web API, which validates the input and
stores the task in the Database. The student can edit or delete a task using the same pattern.
The student can mark a task as done, which updates the task status in the Database. The
student can start a MyCourses sync from the client. The client sends a sync request to the Web
API. The Web API calls the MyCourses Connector, which calls MyCourses web services to
retrieve courses, assignments, and submission status for that user. The connector returns the
ITCS383 Software Construction and Evolution Updated: 26 Jan 2025
Lab week 4
mapped result to the Web API. The Web API creates new imported tasks for new assignments
and updates existing imported tasks when the assignment due date or submission status
changes. When a MyCourses assignment is marked as submitted, the related imported task can
be marked as done automatically or marked with a submitted status, depending on the design
choice. The user then refreshes the task list and sees updated items.
The system has key rules that guide the architecture. Each user can access only their own task
list. Student tasks are private and are not visible to instructors or other students. Imported tasks
must be linked to the MyCourses assignment ID to support update and deduplication.
Synchronisation must not delete manual tasks. Synchronisation failures must not corrupt
existing tasks. The system must handle MyCourses downtime by returning a clear error to the
user and recording the failure in sync history. All network communication must use HTTPS. The
system should store only the minimum MyCourses data needed to support the task view, such
as course name, assignment title, due date, and submission status. The system should keep a
sync log with timestamp, result, and error message for troubleshooting. The admin role can view
sync health and manage system wide settings such as MyCourses endpoint configuration and
default sync frequency.
For C4 Component level within the Web API, the internal design can be decomposed into major
components with clear responsibilities. Authentication and Authorization Component handles
login, token validation, and access control checks. Task Management Component handles
CRUD operations for manual and imported tasks. MyCourses Sync Orchestrator Component
manages the sync workflow and decides when to call external services and how to update
tasks. MyCourses Client Component calls MyCourses web services and handles HTTPS
requests and JSON parsing, and may be implemented inside the MyCourses Connector.
Mapping Component converts MyCourses assignment and submission data into the internal
task model. Sync History Component records sync outcomes and provides data for admin
monitoring. Data Access Component provides repository functions for PostgreSQL access and
ensures that all updates are done in controlled transactions.
## C4 Context Diagram

```mermaid
graph TB
    Student["👤 Student"]
    Instructor["👤 Instructor"]
    Admin["👤 System Administrator"]
    
    TodoList["<b>ICT To Do List System</b><br/>Task Management Platform"]
    
    MyCourses["<b>MyCourses</b><br/>E-Learning Platform<br/>[External System]"]
    
    Student -->|"Uses Web/Mobile App"| TodoList
    Instructor -->|"Monitors assignments"| TodoList
    Admin -->|"Manages configuration"| TodoList
    
    TodoList -->|"Sync assignments & submission status"| MyCourses
    MyCourses -->|"Provides course & assignment data"| TodoList
```

### Context Diagram Explanation

The C4 Context diagram shows the ICT To Do List system as a central component with three user roles and one external system:

- **Students**: Main users who create, manage, and track personal tasks and course assignments
- **Instructors**: Can view teaching-related tasks and monitor assignment deadlines (read-only access)
- **System Administrators**: Manage system configuration, user accounts, and monitor sync health
- **MyCourses**: External e-learning system providing course, assignment, and submission data through web services

The system uses HTTPS for all communication with MyCourses and handles OAuth2/OpenID Connect authentication where available.

---

Lab instructions
Since C4 diagrams use a simple notation, many tools can draw them. In this lab, we will explore
three tools that support a lightweight, model driven approach.
● The first tool is Mermaid in GitHub Codespaces.
● The second tool is the C4InterFlow web playground, where you will export your model
and commit it to GitHub.
● The third tool is IcePanel, which provides a web based interface for creating and
managing C4 diagrams.
