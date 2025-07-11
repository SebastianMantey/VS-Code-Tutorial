




- # Title Bar
    - horizontal bar at the top of the window
    - elements:
        - Menu Bar:
            - provides access to various commands --> ordered by category:
                - File:
                    - commands revolving around files, folders or the window
                - Edit:
                    - commands revolving around editing
                - Selection:
                    - commands revolving around working with [selections or multiple cursors][28]
                - View:
                    - commands revolving around opening the different available views in VS Code and adjusting the appearance or [layout][204]
                - Go:
                    - commands revolving around [code navigation][121]
                - Run:
                    - commands revolving around [debugging][30]
                - Terminal:
                    - commands revolving around the terminal and running [tasks][5]
                - Help:
                    - commands revolving around finding help
            - side note:
                - utility of the Menu Bar:
                    - most of the time, there are probably more convenient ways for executing a respective command --> e.g. creating a new file:
                        - Menu Bar > File > New Text File
                        - [Keyboard Shortcut][126]: Ctrl+N
                        - [Command Palette][120]: "new file"
                        - [Explorer][14] toolbar: New File
                    - however, the Menu Bar can be useful for simply learning about what commands are actually available --> e.g. "Expand Selection" for selecting a whole indented block of code
                        - again, one probably wouldn't use the Menu Bar for executing the command multiple times, but instead one would use the respective keyboard shortcut
        - Navigation Controls:
            - enable navigation through the editor history*:
                - *:
                    - works within files and across files
                - left: go back to previous cursor position
                - right: go forward to following/next cursor position
                    - [code example][29]:
                        - line 39: put cursor on "make_move" --> context menu --> "Go to References"
                        - line 112: put cursor on "cycle" --> context menu --> "Go to Definition"
                        - close the files "itertools.pyi" and "code_navigation.py" again
                        - use the Navigation Controls to move back and forth through the editor history
        - Command Center:
            - search bar in the middle --> provides quick access to all of VS Code's functionality
            - click into search bar --> drop-down list:
                - first section --> different types of commands:
                    - Go to File:
                        - select the command or start typing the name of the file you are looking for --> drop-down list:
                            - first section: recently opened files that fit the search criteria
                                - search example: "not"
                            - second section: all remaining files that fit the search criteria
                            - press Enter to open the respective file
                        - by appending a ":" or "@" to the search, you can specify to which line or symbol you want to go within that file, respectively
                            - search examples:
                                - search for "code" --> highlight "code_navigation.py" --> add ":50" to go to line 50 of that file
                                - search for "code" --> highlight "code_navigation.py" --> add "@" to show a list of available symbols for this file --> type "move"
                        - side notes:
                            - opening multiple files:
                                - press RightArrow --> opens the currently selected file in the background and you can continue selecting files
                            - location of the file:
                                - if the file is not in the root folder, then the respective path is depicted next to the file name
                                - tip: to see all the files within a folder just search for the folder name
                                    - search example: "demonstration_examples"
                            - toolbar when hovering over an entry:
                                - Open to the Side
                                - Remove from Recently Opened
                            - order of the results:
                                - search example: "not"
                                - first section:
                                    - results that contain the exact sequence of characters
                                - second section:
                                    - results that contain the exact sequence of characters
                                    - results that contain the individual characters in the given order*
                                    - results that contain the individual characters in any order*
                                    - *:
                                        - the same or a similar fuzzy-search behavior applies to the other types of commands as well
                    - Show and Run Commands*:
                        - *:
                            - a.k.a. the "Command Palette"
                            - probably the most useful type of command:
                                - in contrast to the other types, which have a specific use case (e.g. opening files, searching for text, etc.), this is a more general purpose type
                                - you can basically search and execute any command (i.e. functionality) of VS Code
                        - select the command or type ">" --> drop-down list:
                            - first section: recently used commands
                            - second section: other commands
                                - i.e. all remaining commands
                            - side note:
                                - gear-icon when hovering: configure keybinding
                        - examples:
                            - editing:
                                - "new file"*
                                    - *: additionally to "recently used" and "other" commands, it also depicts "similar" commands
                                - "add cursor"
                                    - code example:
                                        - ```python
                                            print("hello world")
                                            print("hello world")
                                            ```
                                - "transform to title case"
                                - "run in terminal"
                            - UI:
                                - toggle --> e.g. breadcrumbs, mini-map
                                - preferences:
                                    - color theme
                                    - [Settings][12]
                                    - [Keyboard Shortcuts][126]
                                - collapse folders in [Explorer][14]
                            - "collection" of commands:
                                - debug
                                - terminal
                                - file
                        - side notes:
                            - the Command Palette encompasses the other types of commands --> e.g.:
                                - "Go to File..."
                                - "Go to Symbol in Editor..."
                            - the listed commands are context-specific
                                - example: you have to have an editor open to see "format"-commands
                            - [extensions][7] might add new commands
                                - type the name of an extension to see all available commands --> e.g. "Python" or "Jupyter"
                            - the Command Palette provides an easy way to find specific functionality:
                                - e.g. transforming a Jupyter Notebook into a Python file:
                                    - UI: notebook toolbar > overflow menu > export > Python Script
                                    - Command Palette: type "Jupyter python"
                                - i.e. there is no need to memorize where exactly a specific functionality is within the UI and there is also no need to memorize the exact phrasing of the command
                    - Search for Text:
                        - select the command or type "%" --> enter search term --> drop-down list:
                            - depicts file names and respective search results within those files --> select an entry to jump to the search result in the respective file
                                - search example: "show"
                            - icons to the right:
                                - file --> opens the respective file
                                - magnifying glass --> opens the [Search view][64] already populated with the search term
                        - side notes:
                            - searches across all files of the [workspace][122]
                                - i.e. it is more similar to the [Search view][64] than to the ["search within file"-functionality][123]
                            - search-term starts immediately after the "%"-sign
                                - i.e. there is no space needed
                                - example: search for " show" --> leads to different results compared to searching for just "show"
                    - Open Quick Chat
                        - i.e. [GitHub Copilot][172] feature
                    - Go to Symbol in Editor:
                        - select the command or type "@" --> drop-down list:
                            - depicts all the symbols within the currently active file --> select an entry to jump to the respective symbol within the file
                                - [example file][29]
                            - icon on the right: opens file to the side
                        - side notes:
                            - the drop-down list is searchable
                                - example: type "ma"
                            - add a colon ("@:") to group the symbols by kind
                    - Start Debugging:
                        - select the command or type "debug" and press Space --> drop-down list with different [debugging configurations][146] --> select one and start [debugging][30]
                            - i.e. it is simply another way of starting the debugger
                        - side note:
                            - this approach creates an [automatic launch configuration][27]
                    - Run Task:
                        - select the command or type "task" and press Space --> drop-down list with different [tasks][5] --> select one to run the respective task
                    - More:
                        - select the command or type "?" --> drop-down list with all available types of commands --> e.g.:
                            - ":": go to line/column
                                - [code example][29]
                            - "#": lets you jump to any symbol in the [workspace][122]
                                - doesn't list all symbols, but you can search them
                                - example search: "#s"
                            - "edt": lists opened editors by editor group
                            - "term": shows all opened terminals
                            - "view": lists and opens available views
                    - side note:
                        - accessing commands without a (default) [keyboard shortcut][126]:
                            - rather than clicking into the search bar and selecting a command, it is more convenient to open the "Go to File"-command with Ctrl+P and then type the symbol/keyword of the respective command
                            - examples:
                                - press Ctrl+P and type "%"
                                - press Ctrl+P and type "term" and then Space
                - second section --> recently opened files
                    - i.e. it's the same list that you see, when using the [Go to File][213]-command
        - Copilot Controls:
            - click to open secondary sidebar --> [GitHub Copilot][172] functionality
        - Layout Controls:
            - [Customize Layout][203]-button
            - buttons to toggle the:
                - primary side bar
                - [Panel][10]
                - secondary side bar
        - buttons to minimize/maximize/close window
- # Activity Bar
    - # Explorer
        - workspace:
            - definition: workspace = folder + metadata
            - open/close workspace:
                - [Menu Bar][71]: File > Open Folder*
                    - *: or via the blue "Open Folder"-button in the side bar (if no workspace is opened yet)
                - [Menu Bar][71]: File > Close Folder
                - side note:
                    - VS Code uses the terms "folder" and "workspace" synonymously:
                        - [Menu Bar][71]: File > Close Folder
                        - [Menu Bar][71]: File > Add Folder to Workspace...
            - VS Code works (primarily) "folder-based":
                - explanation:
                    - File Explorer in Windows: access to all files/folders of your system
                    - Explorer in VS Code: only access to the files/folders of the workspace
                - advantage:
                    - VS Code can save the state* of the workspace --> you can easily [switch between workspaces][200] (i.e. projects) and immediately start where you left off
                        - *:
                            - e.g. opened files, layout, folding within files, specific [Settings][194], enabled/disabled [Extensions][7], [debugger launch configurations][146] etc.
                            - the state is saved within the metadata
                - side note:
                    - VS Code can also work "file-based":
                        - you can simply create a new file or open an existing file and start editing --> i.e. there is no need to actually open a folder/workspace
                        - the state of that VS Code instance is temporarily saved --> i.e. only until a workspace is opened or a new file is opened while VS Code is closed
            - accessing files/folders outside of the workspace:
                - either directly open the respective file(s)
                    - e.g. via the File Explorer in Windows
                - or create a multi-root workspace:
                    - [Menu Bar][71] > File:
                        - Add Folder to Workspace
                            - code example:
                                - copy the two folders from [this folder][82] to the Desktop
                                - open "folder_1" as a workspace
                                - add "folder_2" to the workspace
                        - Close Workspace
                            - continuing from the previous code example:
                                - close the workspace --> call the workspace-file* "multi_root"
                                    - *: the state of a multi-root workspace is not automatically saved by VS Code within the metadata, instead it must be saved into a "workspace-file"
                        - Open Workspace from File*
                            - *:
                                - alternative: double-click the workspace-file
                            - continuing from the previous code example:
                                - open the multi-root workspace via the "multi_root" file
                    - side notes:
                        - moving the workspace file to a new location:
                            - [Menu Bar][71] > File > Save Workspace As --> automatically updates the "path" attributes relative to the new workspace file location
                                - continuing from the previous code example:
                                    - copy the "multi_root.code-workspace" file to the Desktop and open it:
                                        - the "path" attributes in the "multi_root.code-workspace" file don't get updated --> "folder_1" is renamed to "Desktop" and contains all the files that are on the Desktop and the files of "folder_2" can't be accessed
                                        - manually change the "path" attributes to "folder_1" and "folder_2" respectively
                                    - delete the "multi_root.code-workspace" file on the Desktop --> open the "multi_root.code-workspace" file within "folder_1" again
                                    - execute the command "Save Workspace As" and save the workspace to the Desktop --> the "path" attributes get updated accordingly
                        - removing a folder from the workspace:
                            - right-click the respective folder --> "Remove Folder From Workspace"
                                - continuing from the previous code example:
                                    - remove "folder_2"
            - workspace trust:
                - a security feature --> ensures safe browsing of unfamiliar code
                - when using VS Code, some functionality (i.e. code) is run automatically in the background --> could be used to hide execution of malicious code
                    - toy-example:
                        - copy [this folder][74] and open it as a workspace --> follow the README
                        - explanation of the exploit:
                            - it makes use of the [Unicode control characters][75] U+202E and U+202C
                            - any characters in between those are rendered in the reverse order --> e.g. "file_g" instead of "g_elif"
                        - to disguise the exploit:
                            - the rendering and highlighting of these control characters in VS Code was automatically deactivated via the workspace settings --> see the ["settings.json"][128] file in the ".vscode" folder
                            - the "malicious" file* was hidden among many other "useful" (and similarly named) files
                                - *: it also contains the control characters in its name --> it is listed at the end because it actually starts with the letter "g"
                - for this reason, VS Code, by default, asks if you trust a workspace (or an individual file) or if you want to open it in "Restricted Mode":
                    - prevents any automatic code execution:
                        - you can safely browse files and then:
                            - decide to (not) trust the folder/files
                            - just copy the parts that you need
                        - important note:
                            - workspace trust can't prevent a [malicious extension][236] from executing code if it simply ignores Restricted Mode --> only install and run extensions that you trust
                    - indicators that you are in Restricted Mode:
                        - banner at the top
                        - badge in the [Status Bar][9]
                    - side note:
                        - you can also edit code in the Restricted Mode
                            - doesn't really make sense because you can't actually run it
                - in order to use the full functionality of VS Code, you need to trust the workspace (or individual file) --> manage trust with "Workspace Trust Editor":
                    - open it via:
                        - "Manage"-button in the banner
                        - "Restricted Mode"-badge in the [Status Bar][9]
                        - [Command Palette][120] --> "Workspaces: Manage Workspace Trust"
                    - disabled functionality of the Restricted Mode is listed:
                        - tasks
                        - debugging
                        - certain settings
                        - certain extensions
                    - activate trust via "Trust"- or "Trust Parent"-button
                        - side note:
                            - you can also deactivate it again via "Don't Trust"-button --> doesn't really make sense because potentially malicious code might have already been executed
                    - already trusted workspaces/folders are listed at the bottom --> toolbar when hovering over an entry:
                        - open file picker
                            - i.e. change the path via the file picker
                        - edit path
                            - i.e. manually change the path
                        - delete path
                    - workflow tips:
                        - [not getting asked for trust all the time][76]:
                            - if a folder is not in the trusted-folders list, VS Code asks if you trust the folder (even if you created it yourself) --> can get annoying
                                - code example:
                                    - create two folders "project_1" and "project_2" --> open them as workspaces respectively
                            - workarounds:
                                - turning the trust-feature off altogether via [Settings][12]: security.workspace.trust.enabled --> not recommended
                                - since "trust" applies to all files and sub-folders within the trusted folder, you can simply set up a parent folder that you trust (e.g. "Desktop") and put all your projects into that --> ONLY open unfamiliar code from an untrusted folder (e.g. "Downloads")
                                    - side note:
                                        - if you open a sub-folder as a workspace in this scenario, then you don't see the "Don't Trust"-button --> that's because it "inherited" the trust from the parent folder
                        - making a decision about trust for large folders:
                            - often times, a folder with unfamiliar code contains hundreds of files --> not practical to inspect them all in "Restricted Mode"
                            - in those cases, the decision to trust the folder is not so much based on the folder itself, but more on the actual creators of the folder --> e.g. what's their reputation, are they known or anonymous, do other people trust them etc.
        - purpose:
            - to browse and manage the files/folders of the project:
                - browse:
                    - files: depicted with respective icons based on the file type
                    - folders: depicted with arrows --> toggle to show/hide files within the folder
                - manage:
                    - clicking:
                        - single-click --> preview the file
                            - indicated by italics
                            - useful for quickly inspecting different files without opening a bunch of files
                            - enable/disable via:
                                - [Settings][12]: workbench.editor.enablePreview
                                - [Editor toolbar][116]
                        - double-click* --> open the file
                            - *: alternatively single-click file and start editing
                        - side notes:
                            - multi-selection:
                                - individual files:  Ctrl+Click
                                - range of files:    Shift+Click
                            - drag-and-drop to move files/folders around
                    - toolbar:
                        - add new file
                        - add new folder
                        - refresh
                        - collapse folders
                            - collapses all folders in the Explorer --> i.e. you don't need to close them individually
                    - context menu:
                        - cut, copy/paste
                        - delete
                        - rename
                        - other useful options (IMO):
                            - reveal in File Explorer
                                - i.e. quickly navigate to the location of a file/folder in the native Explorer
                            - copy absolute/relative file path
        - the different views*:
            - *:
                - provide additional ways of interacting with files
            - open editors-view:
                - shows the opened editors (i.e. files) ordered by group --> the currently active file is highlighted
                - example use case: [if you don't want to use tabs][129]
                - toolbar:
                    - new file
                    - toggle vertical/horizontal editor layout
                    - save all
                    - close all editors --> closes all editors except [pinned editors][127]
                    - side note:
                        - group toolbar:
                            - save all in group
                            - close group --> also closes [pinned editors][127]
            - outline-view:
                - shows the [symbol tree][78] of the currently active file:
                    - examples:
                        - [Markdown file][80]: shows headings --> i.e. a table of contents
                        - [Python file][79]: shows variables, functions, classes
                - clicking on a symbol:
                    - single-click: highlights the respective line in the file (but doesn't jump into the file)
                    - double-click: jumps into the file and selects everything that belongs to the symbol
                        - example:
                            - [Python file][79] --> click "add" or "MyClass1"
                - toolbar:
                    - collapse/expand all
                    - overflow menu:
                        - follow cursor: highlights the respective symbol where the cursor is currently at
                        - filter on type: toggle between highlighting and filtering*
                            - *:
                                - applies to the [search functionality][132]
                                - search example: search for "my" in [this file][79]
                        - different "Sort By"-modes: position, name, category
                - side note:
                    - [Errors and Warnings][168] are also shown (but not Infos)
                        - example:
                            - [Python file][79] --> uncomment "MyClass2"
                            - info:    line 35 --> needs a spellchecker extension
                            - warning: line 38
                            - error:   line 40
            - timeline-view:
                - visualizes time-series events --> e.g. file saves, [Git commits][138] etc.
        - side notes:
            - hidden files/folders:
                - by default, VS Code hides some specific files/folders from the Explorer --> e.g. ".git"-folders
                    - [example folder][83] where the ".git"-folder is not displayed
                - specify which files/folders to hide via [Settings][12]: files.exclude --> use [these glob patterns][21]
                    - example: add "**/*.md" to exclude Markdown files --> exception: when a respective Markdown file is active in the [Editor][13], then it is also shown in the Explorer
            - you can drag-and-drop or copy-paste files from outside VS Code into the Explorer
    - # Search
        - provides search capability across all files of the [workspace*][122]
            - *: if no workspace is opened, then across all opened files
        - search functionality:
            - search results are grouped by file:
                - search example:
                    - "game"
                - if the file is not in the root of the workspace, then the location of the file is shown next to the file name
                - the total number of results for a particular file is listed on the right-hand side --> hover and click "x" to remove file from the search results
                - single-click a result: opens [preview][124] of the file and highlights respective line + result
                - double-click a result: opens the file and selects the respective search result
            - search options:
                - match case
                    - i.e. case-sensitive search
                    - search example: "Game"
                - match whole word
                    - i.e. it doesn't match when there are any letters, numbers or underscores right before or behind the search term
                    - search example: "game" --> e.g. "game_board" is not included in the search results anymore
                - use [regular expressions][81]
            - search details*:
                - *:
                    - toggle with ellipsis ("...") beneath the search box
                - files to include --> search option: toggle searching only in open editors
                    - search example:
                        - search for "game" and use pattern "*.md" to only include Markdown files
                        - create a new Markdown file that contains the word "game" --> close the file --> toggle "Search only in Open Editors"
                - files to exclude --> search option: toggle excluding certain files based on the exclude-settings*
                    - *:
                        - see [Settings][12]: search.exclude --> inherits all glob patterns from the [files.exclude setting][18]
                    - search example:
                        - search for "show" and use pattern "*.md" to exclude Markdown files
                        - toggle "use exclude settings" on/off:
                            - ".sample" files are excluded since they are located within a ".git"-folder, which is a pattern inherited from the "files.exclude"-setting
                            - add pattern "**/*.ipynb" to the "search.exclude"-setting to exclude Jupyter Notebooks
                    - side note:
                        - in the Search view, the "**/"-prefix for the [glob patterns][108] is assumed
                            - continuing from the previous example:
                                - use "*.ipynb" in the "search.exclude"-setting --> doesn't exclude Jupyter Notebooks
                                - use "*.ipynb" in the "files to exclude"-box --> excludes Jupyter Notebooks
            - search editor:
                - how to open:
                    - via toolbar --> opens new search editor
                    - via "Open in editor"-link* --> opens a search editor populated with the current search criteria
                        - *:
                            - located above the search results
                        - search example: "game" --> click the link
                - advantages:
                    - full-sized editor window (and not just the side bar)
                    - syntax highlighting
                    - surrounding lines for context --> top-right corner:
                        - toggle on/off
                        - specify number of surrounding lines 
                    - the search can be saved into a ".code-search"-file
                        - example use case: come back to the search at a later point
                        - continuing from the previous search example:
                            - save the search --> close it
                            - open the ".code-search"-file --> search for "game_board" instead of "game"
                    - search results are editable*
                        - *:
                            - doesn't affect the original file
                        - example use case: adding comments for documentation purposes
                        - continuing from the previous search example:
                            - look at the results for "demonstration_examples\editor\code_navigation.py" --> add comment "maybe we should rename this function?" at the end of line 4*
                - similarities:
                    - search options:
                        - match case
                        - match whole word
                        - regular expressions
                    - search details --> files to include/exclude
                - difference:
                    - no replace-functionality
                - side note:
                    - double-click anywhere in the search results: opens [preview][124] of the file and places cursor at the respective position
        - search-and-replace functionality:
            - toggle via the arrow left to the search field
                - search example:
                    - write "make_move" into the search-field and "execute_move" into the replace-field
                - side note:
                    - single-clicking a result opens a [diff editor][133] for the respective change --> difference: left side = editable
            - replacement possibilities:
                - all instances
                    - button: next to the replace-field
                - all instances in a certain file
                    - button: hover over file name in the list of search results
                - one specific instance
                    - button: hover over the specific search result in the list of search results
            - replace options:
                - preserve case
                    - i.e. adjusts the case of the new text based on the case of the original text
                    - replace example:
                        - write "game" into the search-field and "match" into the replace-field
                        - toggle "Preserve Case" and replace all instances in "code_navigation.py" --> on line 143, the word "Match" is written with a capital "M" and all other instances are written with a lowercase "m"
        - toolbar:
            - refresh
            - clear search results
            - open new search editor
            - view as tree/list
                - search example:
                    - search for "game"
                    - list-view: flat list of the files that contain the search term
                    - tree-view: nested structure of the files that contain the search term --> based on the folder hierarchy of your project
            - collapse/expand all
        - side notes:
            - UpArrow/DownArrow: go through search history
            - searching a [multi-root workspace][134]: search results are additionally grouped by the root folders
                - search example:
                    - [example multi-root workspace][82] --> open it using the "multi_root" workspace-file
                    - search for "test"
    - # Source Control
        - Git support is built-in:
            - VS Code leverages your machine's Git installation --> i.e. you need to install [Git][185] first (at least version 2.0.0)
            - other source control management tools are available via [Extensions][7]
                - examples: click ["Filter Extensions"][135] > Category > SCM Providers
        - setting up a repo:
            - open an existing repo:
                - open a local repo
                    - i.e. [open a workspace][136] that is version controlled with Git --> [example repo][83]
                - clone a remote repo
                    - via blue "Clone Repository"-button in the side bar --> two options:
                        - provide URL
                            - example URL: https://github.com/SebastianMantey/Decision-Tree-from-Scratch
                        - use "Clone from GitHub"-command:
                            - prerequisite: GitHub authentication
                                - login prompt appears when selecting the command --> logout again via [Accounts-icon][137]
                            - command:
                                - lists all of your GitHub repositories
                                - enables search for repos on GitHub within VS Code
                                    - search example: "vs code"
            - create a new repo*:
                - *:
                    - i.e. create a repo out of the currently [opened workspace][136]
                - "Initialize Repository" to create a local repo
                    - code example:
                        - copy this [folder][110] and use it as an example workspace
                - "Publish to GitHub" to create a remote repo
        - inspecting the commit history:
            - (mainly) via Graph-view:
                - hover over a commit --> tooltip:
                    - author, timestamp and commit message*
                        - *:
                            - depicts title and body of the commit message
                        - code example:
                            - copy [this folder][117] and open it as a workspace
                            - hover over commit "add print statement and README"
                    - how many files changed, how many lines were added/deleted
                        - continuing from the previous code example:
                            - hover over commits "add print statement and README" and "add function"
                    - branch name*
                        - *:
                            - if "pointer" of the branch is at that particular commit
                        - continuing from the previous code example:
                            - hover over commit "add class" or "update README"
                    - button to copy the commit ID
                - click a commit --> reveals affected resources:
                    - continuing from the previous code example:
                        - click commit "add print statement and README"
                    - actions:
                        - when hovering on commit --> Open Changes
                            - opens diff(s):
                                - editor toolbar: Collapse/Expand All Diffs
                                - diff toolbar: Open File
                        - when hovering on file   --> Open File
                            - opens the file from that particular commit
                                - continuing from the previous code example:
                                    - click commit "add function" --> "Open File" for "program.py" in commit "add function" and commit "add print statement and README"
                        - clicking a file         --> opens [diff editor][133] for that file
                            - continuing from the previous code example:
                                - click "program.py" within commit "add function" and commit "add print statement and README"
                - right-click a commit --> context menu:
                    - open changes --> i.e. open [diff(s)][181]
                    - checkout (detached)
                    - create branch
                    - create tag
                    - cherry pick
                    - copy commit Id or Message
                - toolbar:
                    - History Item References Picker:
                        - i.e. determine which branches of the repo should be depicted
                        - first section:
                            - All --> all branches get depicted
                            - Auto --> the currently checked-out branch gets depicted
                                - continuing from the previous code example:
                                    - checkout branch "dev"
                        - second section:
                            - lists all branches of the repo --> multiple branches can be selected
                                - continuing from the previous code example:
                                    - select branches "main" and "dev"
                        - side notes:
                            - the currently checked-out branch gets depicted in blue
                                - continuing from the previous code example:
                                    - checkout branch "main"
                            - type to filter the listed options
                                - filter examples: type "a" or "m"
                    - Go to Current History Item:
                        - highlights most recent commit of the currently checked out branch
                        - continuing from the previous code example:
                            - click "Go to Current History Item"
                            - checkout branch "dev"
                            - click "Go to Current History Item"
                    - Fetch
                    - Pull
                    - Publish Branch --> after publishing: Push
                        - continuing from the previous code example::
                            - checkout branch "main" and publish it
                    - Refresh
                    - overflow menu:
                        - toggle to switch between a tree view or list view via overflow menu in the toolbar
                - side notes:
                    - the graph depicts three different branches*:
                        - *:
                            - when using History Item References "Auto"
                            - continuing from the previous code example:
                                - checkout branch "dev" and publish it
                        - the currently checked out branch
                        - its upstream branch (if available)
                        - its base* branch (if available)
                            - *: i.e. "origin/main"
                    - [similar/additional Git history workflows][84] are available via [Extensions][7]
            - (alternatively) via Timeline-view of the [Explorer][14]:
                - in contrast to the Graph-view, it only depicts the commit history of a specific file
                    - i.e. it doesn't depict the commit history of a specific branch or the commit history of the whole repo
                    - code example:
                        - open [this repository][83] as a workspace
                        - look at the Timeline-views of [this file][20] and [this file][22]
                - hover over a commit --> tooltip:
                    - author, timestamp and commit message*
                        - *:
                            - depicts title and body of the commit message
                        - continuing from the previous code example:
                            - hover over commit "initial commit"
                    - how many lines were added/deleted
                        - continuing from the previous code example:
                            - hover over commit "initial commit" and "add, remove and modify a line"
                    - button to open [diff(s)*][181] and button to copy the commit ID
                        - *:
                            - for the whole commit and not just the respective file
                        - continuing from the previous code example:
                            - open the diff for commit "initial commit"
                - click a commit --> opens diff editor:
                    - right side = clicked commit; left side = preceding commit:
                        - continuing from the previous code example:
                            - click commit "add, remove and modify a line"
                        - three types of diffs:
                            - line added:
                                - right side: green highlighting and "+" sign next to line number
                                - left side: additional line is indicated via shaded area (diagonal lines)
                            - line removed:
                                - right side: removed line is indicated via shaded area (diagonal lines)
                                - left side: red highlighting and "-" sign next to line number
                            - line modified:
                                - right side: green highlighting and "+" sign next to line number --> modified part has brighter highlighting
                                - left side: red highlighting and "-" sign next to line number --> modified part has brighter highlighting
                        - side note:
                            - left side = read-only; right side = read-only
                    - toolbar:
                        - file-icon: open the respective file
                        - up/down arrow: move to previous/next diff
                        - pilcrow-icon: toggle for showing leading/trailing whitespace diffs
                            - continuing from the previous code example:
                                - click commit "whitespace + collapse unchanged regions"
                        - map-icon: toggle for collapsing/expanding unchanged regions
                            - see previous code example
                            - side notes:
                                - collapsing/expanding a specific region:
                                    - click "hourglass with arrows"-symbol next to the region to expand it
                                    - click "up-down-arrows"-symbol next to the region to collapse it
                                - sashes of the unchanged region:
                                    - click to reveal a [certain number of hidden lines][240] from the bottom/top of the unchanged region
                                    - drag to manually unveil lines from the bottom/top of the unchanged region
                                - available adjustments via [Settings][12]:
                                    - diffEditor.hideUnchangedRegions.contextLineCount --> adjusts how many lines are used as context around the change
                                        - example: set it to "4" and then "5"
                                    - diffEditor.hideUnchangedRegions.minimumLineCount --> adjusts how many unchanged lines there need to be at a minimum in order to be considered as an unchanged regions
                                        - example: set it to "7" and then "8"
                                    - diffEditor.hideUnchangedRegions.revealLineCount --> adjusts how many lines are revealed when you click the sashes of an unchanged region
                                        - example: set it to "3" and then "5"
                        - overflow-menu --> first section:
                            - toggle "Inline View":
                                - side note:
                                    - if inline view is toggled off but the editor width is too narrow, then inline view is automatically activated --> additional toggle* in the overflow menu appears to adjust this behavior
                                        - *: "Use Inline View When Space Is Limited"
                            - toggle "Show Moved Code Blocks":
                                - indicated via a box around the respective code blocks + arrow between the blocks --> highlighting turns yellow when clicking into the respective blocks
                                    - continuing from the previous code example:
                                        - click commit "moved code block"
                                - compare-button: moves respective code blocks next to each other
                - right-click a commit --> context menu:
                    - open changes --> opens [diff editor][133]
                    - open commit --> opens [diff(s)*][181]
                        - *:
                            - for the whole commit and not just the respective file
                        - continuing from the previous code example:
                            - "open commit" for the "initial commit"
                    - select for compare --> enables comparison of any two commits
                        - continuing from the previous code example:
                            - right-click commit "initial commit" --> "Select for Compare"
                            - right-click commit "whitespace + collapse unchanged regions" --> "Compare with Selected"
                        - side note:
                            - you can actually compare any two files in this way*
                                - *:
                                    - alternatively, you can also select two files --> right-click: "Compare Selected"
                                - code example:
                                    - compare [file 1][22] with [file 2][23] 
                    - copy commit Id or Message
                - toolbar:
                    - Pin the Current Timeline
                        - i.e. timeline-view doesn't update when you switch to another file
                        - continuing from the previous code example:
                            - pin the timeline of [this file][20] --> open [this file][22]
                    - Refresh
                        - see the most up-to-date timeline
                    - Filter
                        - toggle which time-series event(s) should be depicted --> e.g. Git commits, local history* etc.
                            - *: i.e. file saves
                        - continuing from the previous code example:
                            - open [this file][20] and toggle "local history" on/off
                    - Overflow Menu:
                        - restore a file from a previous file save
                            - code example:
                                - ```python
                                    print("hello")
                                    print("world")
                                    ```
                                - preparations:
                                    - open a workspace
                                    - create a new file*
                                        - *: if the file has the same name as a previous file, then the timeline-view actually shows the timeline of that file --> in my case, for example, "test.py"
                                    - add line 1 and save the file
                                    - add line 2 and save the file
                                    - delete the file
                                - restoring the file:
                                    - click the "restore"-option in the overflow menu
                                    - search for the deleted file
                                    - select the first file save
                                    - click the checkmark-button in the editor toolbar
        - creating commits:
            - when files are added/modified/deleted, they get listed in the side bar in the "Changes"-section
                - code example:
                    - copy this [repository][87] and open it as a workspace
                    - delete "file_1.py"
                    - modify "file_2.py":
                        - transform "1" into "100" on line 1
                        - delete line 3
                        - add a new line at the end with "5"
                    - add "file_3.py"
                - side note:
                    - additionally provided info about the changes:
                        - [Source Control icon][214]
                        - side bar/tabs: indications if specific file is untracked*, modified or deleted
                            - *: i.e. it was added
                        - gutter indicators: indications if specific line is added, deleted or modified
            - manage the changes via the different toolbars:
                - individual files:
                    - open file
                    - discard changes
                    - stage changes --> moves file into "Staged Changes"-section*
                        - *: unstage it again with the "-"-button
                - "Changes"-section:
                    - open changes
                        - i.e. open [diff(s)][181] --> additional options:
                            - diff toolbar: stage changes --> for the respective whole file
                            - overflow menu: gutter indicators for staging/reverting code blocks
                    - discard all changes
                    - stage all changes --> moves all files into "Staged Changes"-section
                - "Staged Changes"-section*
                    - *:
                        - i.e. the staging area
                    - open staged changes
                        - toolbar:
                            - unstage changes
                            - open file
                    - unstage all changes
            - when there are staged changes, write the commit message into the input field at the top* --> click blue "Commit"-button** to create the commit
                - continuing from the previous code example:
                    - stage all changes --> commit message:
                        - title: "commit_1"
                        - body: "This is the body of the commit message, which contains more detailed information about the commit."
                - *:
                    - press Enter to create a new line
                - **:
                    - alternatively: Ctrl+Enter
                    - if no commit message was entered into the input field, then VS Code opens an editor for the "COMMIT_EDITMSG" file --> enter the message in that file and confirm
            - side notes:
                - click a file to open the [diff editor][133]
                    - alternatively click "Open Changes" button in the Editor toolbar
                    - when the file is in the:
                        - "Changes"-section: left side = read-only; right side = editable
                        - "Staged Changes"-section: both sides are read-only
                    - there are gutter indicators for staging/reverting code blocks
                - changing the most recent commit:
                    - amending:
                        - via drop-down menu of the "Commit"-button
                        - continuing from the previous code example:
                            - add a line to "file_2.py"
                            - stage the file
                            - commit message: "commit_1 (amended)"
                            - amend the earlier commit
                    - undoing:
                        - via [Command Palette][120]: "Git: Undo Last Commit"
                            - the command puts all the files in the staging area again and you can do whatever changes you want to do
                        - continuing from the previous code example:
                            - run the command
                            - unstage "file_3.py"
                            - delete the last line of "file_2.py" again --> stage the change
                            - rename the commit message to "commit_1" again
                            - create the commit
                - staging only part of a file:
                    - via [Command Palette][120]:
                        - "Git: Stage Selected Ranges"
                            - continuing from the previous code example:
                                - run "Git: Undo Last Commit" via Command Palette
                                - unstage "file_2.py"
                                - highlight line 1 and 4 in "file_2.py" and then run "Git: Stage Selected Ranges"
                    - via gutter indicator(s) in the:
                        - regular Editor:
                            - click a gutter indicator to see an inline diff editor for that particular change
                            - toolbar:
                                - Stage Change
                                - Revert Change
                                - Show Next/Previous Change
                                - Close
                        - [diff editor][237]
                        - ["changes" editor][176]
        - working with branches:
            - via [Command Palette][120] --> some useful commands:
                - "Git: Create Branch..."
                    - code example:
                        - copy this [repository][87] and open it as a workspace
                        - create a branch called "dev"
                - "Git: Checkout to..."
                - "Git: Merge..."
                    - continuing from the previous code example:
                        - merge without merge conflict:
                            - on branch "dev", add a "5" on a new line in "file_1.py" --> create a commit called "dev_1"
                            - checkout branch "main" --> add a "5" on a new line in "file_2.py" --> create a commit called "main_1"
                            - merge "dev" into "main" 
                        - merge with merge conflict:
                            - create the conflict:
                                - checkout branch "dev" --> merge "main" into "dev" --> add a "6" on a new line in "file_1.py" --> create a commit called "dev_2"
                                - checkout branch "main" --> add a "60" on a new line in "file_1.py" --> create a commit called "main_2"
                                - merge "dev" into "main" --> VS Code:
                                    - highlights "Current Change" in green and "Incoming Change" in blue
                                    - moves respective file(s) into "Merge Changes"-section
                                    - creates commit message "Merge branch..."
                            - resolve the conflict:
                                - via inline actions:
                                    - Accept Current Change
                                    - Accept Incoming Change
                                    - Accept Both Changes
                                    - Compare Changes --> opens [diff editor][133]
                                    - side note:
                                        - code is editable --> i.e. you can also manually resolve the conflict
                                - via Merge Editor*:
                                    - *:
                                        - open via "Resolve in Merge Editor"-button
                                    - layout:
                                        - top-left: Incoming Change --> read-only
                                        - top-right: Current Change --> read-only
                                        - bottom: Result --> editable
                                    - inline actions:
                                        - Incoming/Current Change:
                                            - Accept Incoming/Current
                                            - Accept Combination
                                            - Ignore
                                                - just removes the yellow highlighting --> otherwise it doesn't really have an effect
                                        - Result:
                                            - Remove Incoming/Current
                                            - Reset To Base*
                                                - *: available when code was manually edited
                                    - toolbars:
                                        - Incoming/Current Change:
                                            - Accept All Changes From Left/Right
                                            - Compare With Base --> opens [diff editor][133]
                                        - Result:
                                            - Reset
                                        - Editor:
                                            - open file
                                            - go to previous/next conflict
                                            - overflow menu:
                                                - mixed layout/column layout
                                                - show base top/center
                                                - show non-conflicting changes
                                    - "Complete Merge"-button
                            - stage changes* --> create the commit
                                - *: only necessary if merge conflict was resolved via inline actions and not via Merge Editor
                - "Git: Delete Branch..."
                    - continuing from the previous code example:
                        - delete branch "dev"
            - via [Status Bar][9]:
                - click name of the currently checked out branch --> drop-down list:
                    - first section:
                        - Create new branch
                        - Create new branch from
                            - continuing from the previous code example:
                                - create a new branch called "dev" from "main"
                        - Checkout detached
                    - second section:
                        - list of available branches --> click an entry to checkout the respective branch
                - side note:
                    - a "*" next to the branch name serves as a dirty indicator
        - working with a remote*:
            - *:
                - by default the remote is set up on GitHub
                - prerequisite: GitHub authentication --> login prompt appears, for example, when trying to publish a branch via:
                    - blue "Publish Branch"-button in the side bar
                    - "Publish"-button in the [toolbar of the Graph-view][139]
                    - "Publish"-button in the [Status Bar][9]
                - code example:
                    - copy this [repository][87], open it as a workspace and publish branch "main"
            - via [Command Palette][120] --> some useful commands:
                - "Git: Fetch"
                    - continuing from the previous code example:
                        - on GitHub, add a "5" on a new line in "file_1.py" --> create a commit called "commit_1"
                        - fetch the incoming changes
                    - side note:
                        - automatically fetch changes via [Settings][12]:
                            - git.autofetch
                            - git.autofetchPeriod
                - "Git: Pull"
                    - continuing from the previous code example:
                        - pull the incoming changes from GitHub
                - "Git: Push"
                    - continuing from the previous code example:
                        - in VS Code, add a "6" on a new line in "file_1.py" --> create a commit called "commit_2"
                        - push the outgoing changes to GitHub
                - "Git: Sync"*
                    - *:
                        - pulls incoming changes and then pushes outgoing changes
                    - continuing from the previous code example:
                        - on GitHub, add a "7" on a new line in "file_1.py" --> create a commit called "commit_3"
                        - in VS Code, add a "5" on a new line in "file_2.py" --> create a commit called "commit_4"
                        - run "Git: Fetch"
                        - sync the outgoing and incoming changes
                    - side note:
                        - alternatives:
                            - click blue "Sync Changes"-button in the side bar
                            - click "incoming/outgoing changes"-button in the [Status Bar][9]
            - via [toolbar of the Graph-view][139]
            - side notes:
                - the [Github Pull Requests][85] extension provides functionality to manage pull requests and issues from within VS Code
                - other hosting providers for remotes are available via [Extensions][7] --> e.g. [GitLab][141] or [Bitbucket][142]
        - side notes:
            - overflow menu:
                - toggle the different views:
                    - Source Control Repositories:
                        - use case: working with multiple repositories simultaneously
                        - code example:
                            - open [this folder][86] as a workspace
                            - click an entry in the "Source Control Repositories"-view to view the respective repo
                            - side note:
                                - the different repositories could also be managed with different source control providers 
                    - Source Control
                    - Source Control Graph
            - Changes-view toolbar:
                - View as Tree/List
                    - code example:
                        - copy this [repository][87] and open it as a workspace
                        - modify "file_1.py" and "file_2.py"
                        - difference:
                            - tree-view lists the modified files based on their location
                            - list-view simply lists the modified files --> location is written next to the file name (if it is not in the root folder)
                - Commit
                - Refresh
                - Overflow Menu:
                    - "View & Sort"
                        - different sorting options for the changes
                    - list of all available Git commands
                    - "Show Git Output"
                        - opens the [Output-view][143] --> shows which Git commands are actually used under the hood by VS Code
    - # Debugger
        - terminology:
            - bug:
                - a technical error or malfunction
                    - side note:
                        - historical context:
                            - first use of the term with this meaning dates back to (at least) the 1870s --> e.g. Thomas Edison used it 1878 in a [letter to an associate][88]:
                                - "It has been just so in all of my inventions. The first step is an intuition, and comes with a burst, then difficulties arise - this thing gives out and [it is] then that "Bugs" - as such little faults and difficulties are called - show themselves and months of intense watching, study and labor are requisite before commercial success or failure is certainly reached."
                            - later, the term was also adopted in computer science --> famous story from [Admiral Grace Hopper][89]:
                                - while she was working on a Mark II computer at Harvard University in the 1940s, her associates discovered a moth stuck in a relay
                                - the moth was impeding the operation, whereupon she wrote in a log book entry: ["First actual case of bug being found."][90]
            - debugging:
                - the process of fixing technical errors or malfunctions
            - debugger:
                - a tool that allows you to execute a program one line at a time --> you can inspect its state* at any given point --> useful for debugging
                    - *: e.g. values of variables, available functions, classes or modules/packages, etc.
                    - side note:
                        - a debugger can also be a useful tool for programming beginners to understand how exactly a program gets executed --> e.g. when using a recursive function
        - basic functionality*:
            - *:
                - available debugging functionality depends on the specific debugger extension --> i.e. what programming language you are using
            - setting breakpoints:
                - purpose:
                    - when debugging, you are (usually) interested in a specific part of your code
                        - code example:
                            - ```python
                                print("start of program")
                                
                                # create a list of numbers
                                lst = []
                                for i in range(5):
                                    lst.append(i)
                                
                                print("end of program")
                                ```
                            - let's say you are interested in inspecting the variable "lst" after it has been populated within the for-loop
                    - instead of starting the debugger on line 1 and then stepping through the entire program line-by-line until you reach that specific part, you can set a so-called breakpoint
                    - the debugger then simply runs all of the code until it hits that breakpoint and then it pauses the program
                - how to create:
                    - hover over the gutter (left to the line numbers) --> red dot appears --> by clicking you can toggle breakpoint on/off
                    - you can set as many breakpoints as you want
                - Breakpoints-view:
                    - lists all the breakpoints in the [workspace][122] --> depicted with file name, folder location* and respective line number
                        - *:
                            - unless the file is in the root of the workspace
                            - continuing from the previous code example:
                                - set a breakpoint at line 8
                                - set a breakpoint in some file within [this folder][119]
                    - click a breakpoint to quickly get to the respective breakpoint within the file
                        - side note:
                            - toolbar when hovering over a breakpoint:
                                - edit [condition][144]
                                - remove breakpoint
                    - checkbox: deactivates*/activates the respective breakpoint
                        - *: instead of removing it
                    - toolbar:
                        - add [function breakpoint][145]
                        - toggle for activating/deactivating all breakpoints
                            - side note:
                                - an unchecked breakpoint is not affected
                        - remove all breakpoints
            - running the debugger:
                - click "Run and Debug"-button:
                    - opens a drop-down list first, where you need to specify a [debugger and a debug configuration][146]
                        - code example:
                            - ```python
                                print("start of program")
                                
                                # print elements of the list
                                lst = [1, 2, 3]
                                for element in lst:
                                    print(element)
                                
                                print("end of program")
                                ```
                            - set a breakpoint at line 8
                    - then, the debugger will execute the program up until (but not including) the first breakpoint --> indicated by yellow arrow in the gutter and yellow-highlighted line
                - side notes:
                    - alternatively the debugger can be run via:
                        - [Menu Bar][147]
                        - [Editor Play-button][148]
                    - a breakpoint must be set on an executable line*
                        - *:
                            - i.e. not an empty line or a line with just a comment
                        - otherwise debugger stops at last executable line before the breakpoint
                            - continuing from the previous code example::
                                - set breakpoints at line 3 and 7
                    - you can actually also run the debugger without setting any breakpoints
            - ["execute a program one line at a time"][149] via the debug toolbar:
                - continue:
                    - continue executing the program until next breakpoint* is reached
                        - *:
                            - "next breakpoint" can actually be the same breakpoint --> e.g. within a for-loop
                            - if there is no other breakpoint, then the program continues until completion
                        - [code example][91]:
                            - set breakpoints at line 6 and 18
                - step over:
                    - execute highlighted line + go to next line in the current scope
                        - i.e. without going into the scope of functions/methods, classes or modules
                        - [code example][91]:
                            - set breakpoint at line 10 --> step over until line 38
                    - exception: there is a breakpoint somewhere in the deeper scope(s)
                        - [code example][91]:
                            - set breakpoint at line 10
                            - set breakpoints at lines 11 and 26*
                                - *: i.e. breakpoints within the scope of a function and method
                            - set breakpoint at line 23*
                                - *: i.e. a breakpoint within the scope of a class
                            - set breakpoints at lines 2 and 4 in [this file][92]*
                                - *: i.e. breakpoints within the scope of a module
                            - step over until line 38
                - step into:
                    - go into the scope of functions/methods, classes or modules --> applicable when a function/method is called, a class is defined or a module is imported
                        - [code example][91]:
                            - set breakpoint at line 10
                            - step into the function at line 17
                            - step into the class at line 22
                            - step into the method at line 30
                            - step into the module at line 34
                    - side note:
                        - if there is no scope to step into, then "step into" behaves like "step over"
                            - [code example][91]:
                                - set breakpoint at line 10 --> "step in"
                - step out:
                    - execute remaining lines of the current scope and return to outer scope*
                        - *:
                            - i.e. you don't have to "step over" each individual line
                        - [code example][91]:
                            - set breakpoint at line 10
                            - step into the function at line 14 --> step out of the function*
                                - *:
                                    - debugger goes back to the point where the return-value is about to be returned
                            - step into the class at line 22 --> step over one line and then step out of the class*
                                - *:
                                    - debugger goes back to the point where the class is about to be created
                            - step into the module at line 34* --> step out of the module
                                - *:
                                    - (Python-specific) notification: "Frame skipped from debugging during step-in"
                                    - problem: debugger actually stops when you "step out"
                                    - workarounds:
                                        - "step over" each line in "my_module.py"
                                        - set a breakpoint in "basic_functionality.py" after the import statement  (e.g. at line 38) --> "step out"
                                        - disable the ["Just My Code"-setting][150] --> "step over" each line in "__init__.py" --> now "step out" works as intended
                    - side note:
                        - if there is no outer scope, then "step out" behaves like "stop"
                            - [code example][91]:
                                - set breakpoint at line 10 --> "step out"
                - restart:
                    - restart the debugger from the beginning
                - stop:
                    - stop the debugger
                - side notes:
                    - the "continue" button also serves as a "pause" button:
                        - pauses currently running program --> regardless of breakpoints
                            - code example:
                                - ```python
                                    import time
                                    
                                    print("start of program")
                                    
                                    x = 2
                                    for i in range(30):
                                        print(x**i)
                                        time.sleep(1)
                                    
                                    print("end of program")
                                    ```
                                - set breakpoint at line 3
                        - peculiarity: you can't inspect the program's state when pausing the debugger --> e.g. the [Variables-view][198] is empty
                        - workaround: "step over" one line
                    - move the toolbar left/right and up/down* with the handle on the left-hand side
                        - *: lowest possible position --> right below the tabs
            - ["inspect its state"][149] via the different views:
                - Variables:
                    - displays the program's current variables --> broken down into global and local variables
                        - [code example][91]:
                            - set breakpoint at line 14
                            - note: when the debugger is in the global scope, then "Locals" and "Globals" are the same
                            - step into "square" to create a local scope
                            - step over one line to create the variable "result"
                            - step out of "square"
                    - the different "types" of variables listed:
                        - special variables
                            - [code example][91]:
                                - set breakpoint at line 4
                            - variables that are not directly part of the program but that are built into Python itself --> e.g. "__name__" or the built-in function "len()"
                        - "basic" variables
                            - continuing from the previous code example:
                                - step over until line 10
                                - note: data structures can be further inspected via drop-down arrow
                        - function variables
                            - continuing from the previous code example:
                                - step over to line 14
                            - side note:
                                - when a function is called, the return-value is also listed --> but only when using "step over" or "step into/out" and not "continue"
                                    - continuing from the previous code example:
                                        - step over "square" at line 14
                                        - step into "square" at line 17 --> step out of it again
                                        - set breakpoint at line 18 --> restart the debugger and continue to the this breakpoint
                        - class variables
                            - continuing from the previous code example:
                                - step over until line 29
                            - side note:
                                - when a class is initialized, the return-value is also listed --> but only when using "step over" or "step into/out" and not "continue"
                                    - continuing from the previous code example:
                                        - delete breakpoint at line 18
                                        - set breakpoint at line 29 --> restart the debugger and "continue" to the this breakpoint
                        - modules
                            - continuing from the previous code example:
                                - step over until line 35
                    - side notes:
                        - inline values:
                            - the values of the respective variables are also depicted directly in the file itself* --> yellow background highlighting
                                - *: next to where the variable was assigned or where the variable was referenced the last time
                        - hover over a variable in the file to see its value
                            - continuing from the previous code example:
                                - hover over:
                                    - "lst" on line 5
                                    - "x" on line 15
                                    - "square" on line 17
                                    - "instance" on line 29
                                    - "my_module" on line 35
                        - toolbar --> collapse all
                        - right-click a variable:
                            - set value
                                - [code example][91]:
                                    - set breakpoint at line 15
                                    - set the value of "x" equal to "0" --> step over to print it out
                            - copy value
                            - copy as expression
                            - add to [watch][17]
                - Watch:
                    - enables you to more easily keep track of specific variables/expressions*
                        - *:
                            - useful when the Variables-view gets cluttered due to a large number of different variables
                        - [code example][91]:
                            - set breakpoint at line 15 --> right-click "x" in the Variables-view and "Add To Watch" --> step through the program
                    - toolbar:
                        - Add Expression
                            - [code examples][91]:
                                - set breakpoint at line 15
                                - applying an operator to a variable --> x**2
                                - slicing a list --> lst[:2]
                                - calling a function --> max(lst); square(element)
                                - accessing a method/attribute --> lst.count(3)
                            - side note:
                                - right-click an expression to edit it
                                    - continuing from the previous code example:
                                        - change the expression "lst[:2]" to "lst[:3]"
                        - Remove All Expressions
                            - side note:
                                - alternatively, hover over a specific expression and click the "x" to remove it
                        - Collapse All
                - Call Stack:
                    - displays the order in which the program's subroutines* were called --> current one at the top
                        - *:
                            - i.e. which functions/methods, classes or modules
                        - [code example][91]:
                            - set breakpoint at line 22
                            - step into "SomeClass" --> step over one line
                            - step into "square"
                    - displayed information:
                        - name of the function/method/class or "<module>"*
                            - *: if subroutine is in the global scope of a file
                        - file name
                        - line number and column number
                    - side notes:
                        - click an entry --> jump to respective subroutine:
                            - indicated via green arrow and highlighting --> exception: current subroutine keeps yellow arrow and highlighting
                            - Variables- and Watch-view change accordingly
                                - continuing from the previous code example:
                                    - select subroutine "square" --> add "number" to Watch-view
                                    - select subroutine "<module>"
                        - right-click --> copy call stack
                        - toolbar:
                            - Collapse All
                - side note:
                    - overflow menu:
                        - toggle debug console or the different views
            - using the debug console:
                - location:
                    - in the [Panel][10]
                - purpose:
                    - lets you interactively write code based on the program's current state
                        - [code example][91]:
                            - set breakpoint at line 15 --> example expressions:
                                - lst
                                - lst[0]
                                - square(5)
                                - x = 0 --> step over to see that it prints "0"
                                - instance.some_method() --> error because "instance" is not defined yet
                            - step over until line 38 --> example expressions:
                                - instance.some_method()
                                - my_module.function_1()
                            - side note:
                                - you can also, of course, write just any code that is not directly related to the program --> e.g. "1 + 1"
                    - displays messages from [logpoints][151]
                - controls:
                    - Enter: run code
                    - Shift+Enter: new line
                        - code example:
                            - ```python
                                for i in range(5):
                                    print(i)
                                ```
                    - Tab: select entry from member list
                    - UpArrow/DownArrow: cycle through command history
                - toolbar:
                    - input box:
                        - filter debugging output --> i.e. [messages from logpoints][152]
                    - search:
                        - search across the debug console
                            - [code example][91]:
                                - set breakpoint at line 38
                                - run the following expressions in the debug console:
                                    - square(5)
                                    - my_module.function_1()
                                    - my_module.function_2()
                                    - my_module.function_1()
                                - search for "my" --> navigate through search results via UpArrow/DownArrow
                        - options:
                            - toggle filter
                                - continuing from the previous code example: toggle filter on/off
                                - side note:
                                    - the output doesn't get highlighted, but it is nonetheless considered when filter is applied
                                        - continuing from the previous code example: search for "func" and toggle filter on
                            - toggle fuzzy search
                                - continuing from the previous code example:
                                    - search for "funcn"
                                    - toggle toggle between fuzzy search or exact search
                    - clear console
            - side notes:
                - multiple debugger sessions:
                    - you can run multiple debugger sessions [simultaneously][179]
                        - code example:
                            - set breakpoint at line 1 in [this file][91] --> start debugger
                            - set breakpoint at line 1 in [this file][92] --> [start debugger][175]
                    - to switch between sessions a dropdown menu appears here:
                        - debug toolbar*
                            - *: alternatively, navigate the sessions via the Call Stack view
                        - debug console
                - non-workspace debugging:
                    - debugging also works without creating/opening a [workspace][122] --> difference: [launch configurations][146] can't be managed
                - "Just My Code"-setting:
                    - [Settings][12]: debugpy.debugJustMyCode
                    - enabled by default
                        - i.e. by default the debugger only considers user code and not library code
                    - if the setting is disabled, then:
                        - you can step into library code
                            - code example:
                                - ```python
                                    import random
                                    
                                    random_number = random.randint(1, 10)
                                    print(random_number)
                                    ```
                                - set breakpoint at line 3
                                - step into "randint" while "Debug Just My Code"-setting is enabled/disabled
                        - the traceback for an exception goes into library code* --> accessible via Call Stack-view
                            - *:
                                - see also this [side note][154] for a better understanding
                            - continuing from the previous code example:
                                - line 3:
                                    - remove breakpoint
                                    - transform the ten into a string
                                - set breakpoint at line 4
                                - start the debugger while "Debug Just My Code"-setting is enabled/disabled
        - advanced functionality*:
            - *:
                - available debugging functionality depends on the specific debugger extension --> i.e. what programming language you are using
            - different types of breakpoints:
                - conditional breakpoints:
                    - how to create:
                        - right-click gutter --> "Add Conditional Breakpoint..."
                        - right-click existing breakpoint --> "Edit Breakpoint..." --> select "Hit Count" or "Expression" from the drop-down menu
                    - they get triggered when a certain condition is met:
                        - hit count* --> i.e. whenever the breakpoint got hit the specified number of times
                            - *: can be combined with the operators ==, >, >=, <, <=, and %
                        - expression --> i.e. whenever the given expression evaluates to true
                            - code examples:
                                - ```python
                                    for i in range(1000):
                                        print(i)
                                    ```
                                - set conditional breakpoint at line 1:
                                    - set a hit count of 5 --> press continue
                                    - change the hit count to "<5" --> press continue multiple times
                                    - add the expression "300 < i < 305" --> press continue multiple times
                                    - delete the expression again --> confirm with Enter
                                    - change the hit count to "%10" to break every 10th time the breakpoint gets hit
                    - icon: red circle with equal sign --> hover over it to see conditions
                - logpoints:
                    - purpose:
                        - they don't stop the program but print out a log message to the [debug console][153]
                        - they are like print-statements but without the program itself actually printing something out --> i.e. you don't have to go through the program and delete all print statements after you are done with debugging
                    - how to create:
                        - right-click gutter --> "Add Logpoint..."
                        - right-click existing breakpoint --> "Edit Breakpoint..." --> select "Log Message" from the drop-down menu
                    - usage:
                        - log messages are plain text --> expressions are placed into curly braces
                            - code example:
                                - ```python
                                    import random
                                    
                                    random.seed(4)
                                    lst = []
                                    for i in range(5):
                                        random_number = random.randint(-10, 10)
                                        lst.append(random_number)
                                    ```
                                - add logpoint at line 7 --> log message: "random number: {random_number}"
                        - they can be combined with conditional breakpoints
                            - continuing from the previous code example:
                                - right-click logpoint
                                - edit logpoint
                                - select "Expression" from the drop-down menu --> expression: "random_number < 0"
                        - side note:
                            - you can filter the log messages via the input box in the debug console's toolbar
                                - code example:
                                    - ```python
                                        import random
                                        
                                        random.seed(4)
                                        lst = []
                                        for i in range(5):
                                            random_number = random.randint(-10, 10)
                                            lst.append(random_number)
                                            pass  # dummy line for logpoint
                                        
                                        print(lst)
                                        ```
                                    - add logpoint at line 7 --> log message:
                                        - "random number: {random_number}"
                                    - add logpoint at line 8 --> log message:
                                        - "max value: {max(lst)}"
                                        - press Shift+Enter to add a new line: "----------"
                                    - set breakpoint at line 10
                                    - filter for "random" and then "max"
                                - side notes:
                                    - filter doesn't affect expressions
                                        - continuing from the previous code example:
                                            - type "random_number" into debug console and filter for "random" and then "max"
                                    - filter also applies to output from print-statements
                                        - continuing from the previous code example:
                                            - type "print('max')" into debug console and filter for "max" and then "random"
                    - icon: red diamond-shape --> hover over it to see log message
                - triggered breakpoints:
                    - how to create:
                        - right-click gutter --> "Add Triggered Breakpoint..."
                        - right-click existing breakpoint --> "Edit Breakpoint..." --> select "Wait for Breakpoint" from the drop-down menu
                    - they get triggered once another breakpoint got hit --> useful for debugging failure cases that happen only after a certain precondition
                        - code example:
                            - ```python
                                some_inputs = ["Hello", "World", True, "Hello", "World", 1]
                                
                                list_strings = []
                                for string in some_inputs:
                                    if isinstance(string, str):
                                        string = string.lower()
                                    else:
                                        string = str(string) + "*"
                                    
                                    list_strings.append(string)
                                ```
                            - explanation of the program:
                                - let's say we get some inputs --> we expect them to be strings but we don't know beforehand if they actually are strings
                                - the program should transform those strings into lowercase --> if the input is not a string, then it should transform that input into a string and add an "*" to indicate that this input originally wasn't a string
                                - lastly, the string should be appended to "list_strings"
                            - setting breakpoints:
                                - let's say we are interested in the inputs that are not strings --> we want to know what they look like before we transform them into strings (line 8) and after we transformed them into strings (line 10)
                                - using basic breakpoints --> problem: debugger stops at line 10 for every iteration of the for-loop even though we are only interested in the inputs that were originally not strings
                                - to get around this problem, set a triggered breakpoint at line 10 that only gets triggered once the breakpoint on line 8 got hit
                            - side note:
                                - triggered breakpoints can be used in combination with conditional breakpoints
                                    - continuing from the previous code example:
                                        - let's say we are satisfied with how Booleans are handled and we don't want the debugger to stop if there is a Boolean
                                        - to implement that, transform the breakpoint at line 8 into a conditional breakpoint --> expression: "not isinstance(string, bool)"
                    - icon: red circle with equal sign --> hover over it to see trigger condition
                - function breakpoints:
                    - how to create:
                        - click "+" in the [Breakpoints-view][173] toolbar --> type in function name
                    - they get triggered every time the specified function is called --> debugger steps into the function definition
                        - code example:
                            - ```python
                                def add_one(x):
                                    return x + 1
                                
                                x = 0
                                x = add_one(x)
                                x = add_one(x)
                                x = add_one(x)
                                ```
                            - press continue until debugger stops
                    - they can be combined with conditional breakpoints --> hover over the function breakpoint in the Breakpoints-view and click "Edit Condition"
                        - continuing from the previous code example:
                            - "Edit Condition": x > 0 --> press continue until debugger stops --> delete condition again
                            - "Edit Hit Count": 2 --> press continue until debugger stops
                    - icon: red triangle --> only in the Breakpoints-view and not in the gutter
                - exception breakpoints:
                    - how to create:
                        - exception breakpoints can't be created, they can only be enabled/disabled --> they are listed at the top of the Breakpoints-view
                    - they get triggered when an exception is raised* --> three different types:
                        - *:
                            - i.e. when an error occurs
                        - raised exceptions:
                            - debugger pauses the program at every exception*
                                - *:
                                    - i.e. it even pauses when an exception is accounted for via a try-except block
                                - code example:
                                    - ```python
                                        print("start of program")
                                        
                                        user_input_1 = 1
                                        user_input_2 = 0
                                        
                                        try:
                                            result = user_input_1 / user_input_2
                                        except ZeroDivisionError:
                                            result = "undefined"
                                        
                                        print("end of program")
                                        ```
                                    - set breakpoint at line 11
                                    - disable all exception breakpoints --> debugger pauses at line 11 because there is no exception/error
                                    - enable "Raised Exceptions" --> debugger pauses at line 7
                        - uncaught exceptions:
                            - debugger only pauses the program at uncaught exceptions*
                                - *:
                                    - i.e. it doesn't pause when an exception is accounted for via a try-except block
                                - continuing from the previous code example:
                                    - disable "Raised Exceptions" and enable "Uncaught Exceptions" --> debugger pauses at line 11 again because the ZeroDivisionError is accounted for
                                    - line 4: turn the zero into a string --> debugger pauses the program at line 7 because the TypeError is not accounted for
                            - side note:
                                - by default, "Uncaught Exceptions" are enabled:
                                    - otherwise the debugger doesn't pause, but just stops if there is any uncaught exception
                                        - continuing from the previous code example:
                                            - disable "Uncaught Exceptions" --> debugger stops and there is an error message in the terminal
                                    - and this is not the behavior that you want because if there is any uncaught exception, then you want to investigate why it actually occurred
                        - user uncaught exceptions:
                            - debugger only pauses the program at uncaught exceptions that originate from user code (not library code)*
                                - *:
                                    - i.e. it doesn't pause when there is an uncaught exception in library code --> but only if the uncaught exception doesn't propagate back to user code
                                - code examples:
                                    - prerequisites:
                                        - disable the ["Just My Code"-setting][150]
                                            - if you are just considering user code, then every "uncaught exception" automatically is an "user uncaught exception"
                                            - see also this [side note][154] for a better understanding
                                        - copy [my_library_code.py][93] into the same directory as "random.py"
                                            - this way "my_library_code.py" is treated as library code by the debugger --> make sure to delete it again afterwards
                                            - to find out, where "random.py" is located, run the following code:
                                                - ```python
                                                    import random
                                                    print(random.__file__)
                                                    ```
                                    - uncaught exception in library code that propagates back to user code:
                                        - ```python
                                            import my_library_code
                                            
                                            print("start of program")
                                            my_library_code.function_1()
                                            print("end of program")
                                            ```
                                        - set breakpoint at line 5
                                        - the debugger behaves the same regardless of whether "Uncaught Exceptions" or "User Uncaught Exceptions" are enabled
                                    - uncaught exception in library code that doesn't propagate back to user code:
                                        - continuing from the previous code example: change "function_1" to "function_2"
                                        - "Uncaught Exceptions" enabled --> debugger pauses at line 4* because there is an exception in the thread**
                                            - *: see Call Stack view --> MainThread --> <module>
                                            - **: see Call Stack view --> Thread-6 --> function_1
                                        - "User Uncaught Exceptions" enabled --> debugger skips line 4 and pauses at line 5 
                    - side note:
                        - [slides illustrating the relationship between the different exception breakpoints][118]
                            - purpose:
                                - to make the distinction between the the different types of exception breakpoints more clear
                            - side note:
                                - when multiple exception breakpoints are enabled, then the one that encompasses more exceptions effectively applies
                - side notes:
                    - inline breakpoints:
                        - they get triggered when a specific column in the code is hit
                        - they are not available for Python --> [JavaScript example][94]
                    - data breakpoints:
                        - they get triggered when the underlying value of a variable changes, is read or is accessed
                        - they are not available for Python --> [C++ example][95]
            - launch configurations:
                - prerequisite:
                    - a [workspace][122] needs to be opened/created
                - purpose:
                    - enable you to configure and save debugging setup details
                    - e.g.:
                        - specifying the application entry point
                        - attaching to a running application
                        - setting environment variables
                        - it is also not necessary anymore to manually specify the:
                            - debugger when debugging a new file
                            - debug configuration when (re-)opening a workspace
                                - code example:
                                    - copy [this folder][119] and open it as a workspace
                                    - set a breakpoint in two different files:
                                        - start debugging the first file --> stop --> start again
                                        - start debugging the second file
                                    - close and re-open the workspace:
                                        - start debugging the first file
                                        - start debugging the second file
                - two types:
                    - automatic:
                        - how to create:
                            - click the "Show automatic Python configurations"-button --> select a launch configuration
                                - continuing from the previous code example:
                                    - create an automatic debug configuration --> "Python Debugger: Python File"
                                    - start and stop debugging the opened files
                                    - open the third file in the workspace and set a breakpoint --> start debugging
                                    - re-open the workspace --> start debugging
                        - side notes:
                            - changes in the side bar after creating an automatic debug configuration:
                                - the different views stay visible and the blue "Run and Debug"-button is not depicted anymore*
                                    - *:
                                        - exception: re-opening the workspace
                                - to start debugging, click the green play-button at the top
                            - creating multiple configurations:
                                - click the drop-down arrow next to the green play-button at the top of the side bar --> select an additional configuration*
                                    - *:
                                        - "Node.js" or "Python Debugger" --> "Add Configuration" is for adding a [manual/customized][140] launch configuration
                                    - continuing from the previous code example:
                                        - create a JavaScript file "test.js"
                                            - ```javascript
                                                for (let i = 0; i < 5; i++) {
                                                    console.log(i);
                                                }
                                                ```
                                        - set a breakpoint on line 2
                                        - start debugging --> Syntax Error and debugger stops since you can't debug a JavaScript file with a Python debugger
                                        - click the drop-down arrow --> select "Node.js" --> select "Run current file"
                                        - click "Run and Debug"-button
                                - switch between configurations via the drop-down arrow
                                    - continuing from the previous code example:
                                        - select a Python file --> start debugging --> doesn't work
                                        - select a Python file --> click the drop-down arrow and select "Python Debugger: Python File" --> start debugging
                            - deleting configurations:
                                - the automatic configurations actually can't be deleted 
                                - workaround: copy the folder and open the copied folder as a workspace
                                    - continuing from the previous code example:
                                        - copy the folder --> delete the old one --> rename the copied folder so that it has the name of the original folder
                                        - open the folder as a workspace --> open a Python file and set a breakpoint
                                        - click the "Run and Debug"-button --> there are no more configurations listed next to the green play-button and it  says "No Configurations" again
                    - manual/customized:
                        - workspace-specific:
                            - how to create:
                                - click "create a launch.json file"-link in the side bar --> select a debugger and a debug configuration from the drop-down list
                                    - continuing from the previous code example:
                                        - select "Python Debugger" and then "Python File"
                                        - change the value of attribute "name" to "my config" --> gets depicted next to green play-button
                            - lists of available attributes for customizing:
                                - [general][96]
                                - [Python-specific][97]
                                - side note:
                                    - available attributes can also be accessed via [IntelliSense][155]
                                        - continuing from the previous code example:
                                            - add attribute "justMyCode" --> set to false
                            - side notes:
                                - launch.json is saved into {workspace folder}/.vscode
                                - creating multiple configurations:
                                    - three options:
                                        - click "Add Configuration..."-button at the bottom-right of the launch.json file
                                        - click the drop-down arrow next to the green play-button at the top of the side bar --> "Add Configuration"
                                        - via [IntelliSense][155]
                                            - continuing from the previous code example:
                                                - add a configuration --> select "Python Debugger" and then "Python File with Arguments"
                                    - switch between configurations via the drop-down arrow
                                - deleting configurations:
                                    - simply delete the configuration from the launch.json file
                                        - continuing from the previous code example:
                                            - delete "Python Debugger: Current File with Arguments"-configuration again
                        - user-specific*:
                            - *:
                                - apply globally --> i.e. apply to all workspaces
                            - how to create:
                                - open the [settings.json][128] file --> add the "launch" attribute
                                    - continuing from the previous code example:
                                        - delete the ".vscode"-folder --> start debugging --> it again says "No Configurations" next to the green play-button
                                        - open the settings.json file* --> invoke [IntelliSense][155] --> select the "launch" attribute
                                            - *:
                                                - alternatively open [Settings][12] --> search for "launch" --> click "edit in settings.json" --> select "version"
                                        - put the cursor into the brackets of the "configurations" attribute --> press Enter --> add a configuration via [IntelliSense][155]: "Node.js: Attach"
                                        - open an additional workspace --> the launch configuration is also available there --> close it again
                            - customization is done in the same way as with "workspace-specific" launch configurations
                                - continuing from the previous code example:
                                    - change the value of attribute "name" to "my config"
                                    - add another attribute via [IntelliSense][155] --> e.g. "restart"
                                    - add another configuration:
                                        - add a coma after the closing-braces of the already created configuration --> press Enter
                                        - invoke [IntelliSense][155] --> select "Node.js: Attach to Process"
                                        - peculiarity:
                                            - "Python Debugger" is not listed as an available configuration via [IntelliSense][155]
                                            - however, you can manually* create a Python configuration since all the Python-specific attributes are actually available --> e.g. "django" or "justMyCode"
                                                - *: i.e. manually add a "{}" to the "configurations" attribute and enter all the attributes that you need
                                    - delete a configuration:
                                        - delete the "my config" configuration again
                                        - delete the whole "launch" attribute again
                - side note:
                    - the [Status Bar][9] shows the current configuration --> click to switch the configuration and/or start debugging
    - # Extensions
        - # Jupyter
            - prerequisite:
                - the [extension itself][68] is not a Jupyter Kernel --> you need to install the respective [kernel][41] for your specific programming language
                - examples:
                    - Julia: IJulia
                    - Python: IPyKernel
                        - side note:
                            - you can also just install [Jupyter Notebook][38], [JupyterLab][39] or the whole [Jupyter package][40] with your package manager of choice --> they all contain IPyKernel
            - Jupyter Notebook:
                - initiating a notebook:
                    - creating a notebook:
                        - [Command Palette][120] --> "Create: New Jupyter Notebook"
                        - create a new file and save it with the ".ipynb" file extension*
                            - *: "ipynb" stands for IPython Notebook --> [Jupyter][42] was spun off from IPython
                    - selecting a kernel:
                        - before you can run any code, you need to select a kernel from the kernel picker in the top-right corner
                - notebook toolbar:
                    - first section:
                        - Generate
                            - i.e. [GitHub Copilot][172] feature
                        - Add Code Cell
                        - Add Markdown Cell
                        - side note:
                            - hover at the bottom of a cell: "Generate", "Add Code Cell" and "Add Markdown Cell" buttons appear --> for the very first cell, they also appear when hovering at the top of the cell
                    - second section:
                        - Run All --> Interrupt
                            - code example:
                                - cell 1:
                                    - ```python
                                        print("hello world")
                                        ```
                                - cell 2:
                                    - ```python
                                        import time
                                        
                                        for i in range(50):
                                            print(i)
                                            time.sleep(1)
                                        ```
                        - Restart
                            - restarts the kernel --> i.e. clears the state of the notebook
                            - continuing from the previous code example:
                                - print out "i" --> before and after restarting the kernel
                            - example use case:
                                - when you're done with working on your notebook --> "restart" + "run all" to check if code works as expected
                        - Clear All Outputs
                        - Go-To (currently running or most recently failed cell)
                    - third section:
                        - Jupyter Variables:
                            - button opens the Jupyter-view of the [Panel][10] --> lists a table with the variables defined in the current Jupyter session
                                - code example:
                                    - ```python
                                        message = "Hello World!"
                                        number_1 = 1
                                        number_2 = 1.5
                                        number_3 = 2
                                        ```
                            - variables can be sorted by "Name" or "Type" in alphabetical/reverse-alphabetical order --> click respective column header
                            - the view updates automatically as new variables are created
                                - continuing from the previous code example:
                                    - ```python
                                        number_4 = 2.5
                                        ```
                            - side note:
                                - some variables allow a more detailed inspection via a Data Viewer:
                                    - continuing from the previous code example:
                                        - ```python
                                            list_of_names = ["Alice", "Bob", "Chris", "David", "Eva"]
                                            ```
                                    - click "new tab"-button left to the variable name* --> prompt to show recommended Data Viewer Extensions --> e.g. [Data Wrangler][101]
                                        - *: alternatively, double-click the row
                        - Outline
                            - opens [Outline-view][166]
                    - overflow menu:
                        - export:
                            - exports the notebook as a:
                                - [Python file][161]
                                - HTML file*
                                    - *: needs [jupyter_contrib_nbextensions][44]
                                - PDF file*
                                    - *:
                                        - needs [TeX][45]
                                        - SVG graphics will not be displayed --> workaround: first export to HTML and then print/save as PDF using your browser
                        - Customize Notebook Layout:
                            - opens [Settings][12] --> filtered down to settings related to the notebook layout
                        - toggle breadcrumbs*
                            - *: applies to all files, not just Jupyter Notebooks
                        - toggle line numbers
                - code cells:
                    - cell toolbar:
                        - Run by Line:
                            - requires [IPyKernel 6+][46]
                            - lets you execute a cell one line at a time*
                                - code example:
                                    - ```python
                                        for i in range(5):
                                            print(i)
                                        ```
                                - *:
                                    - i.e in combination with the the [Jupyter-view][162], it's a lightweight debugger
                            - actions:
                                - continue execution
                                    - i.e. run all remaining lines
                                - run next line
                        - Execute Above Cells:
                            - executes all cells above the cell (but not the cell itself)
                                - code example:
                                    - ```python
                                        print("hello world")
                                        ```
                                    - create three cells --> select the last and run all above
                        - Execute Cell and Below:
                            - executes the cell and all cells below it
                                - continuing from the previous code example:
                                    - clear all outputs --> select the first cell and run cell and all below
                        - Split Cell:
                            - splits the cell based on the current cursor position --> everything after the cursor gets split into the next cell
                                - code example:
                                    - ```python
                                        def square(x):
                                            return x**2
                                        
                                        value_1 = 1
                                        value_2 = 2
                                        value_3 = 3
                                        
                                        print(square(value_1))
                                        print(square(value_2))
                                        print(square(value_3))
                                        ```
                                    - split the definition of the function, the instantiations of the variables and the print statements into separate cells
                            - side note:
                                - you can join cells via the overflow menu --> "Join With Previous Cell" or "Join With Next Cell"
                                    - continuing from the previous code example:
                                        - join the cells again
                        - overflow menu:
                            - sections 1 - 3: (mainly) just actions regarding cells where it is easier to use the respective [keyboard shortcut][163] instead
                            - section 4: actions regarding [Jupyter Slide Show][164]
                            - section 5: actions regarding [Jupyter Cell Tags][165]
                            - section 6: toggle cell line numbers + toolbar position
                        - Delete Cell
                    - play-button (left to the cell):
                        - Execute Cell --> Stop Cell Execution
                            - code example:
                                - ```python
                                    import time
                                    
                                    for i in range(50):
                                        print(i)
                                        time.sleep(1)
                                    ```
                        - dropdown menu: Debug Cell --> full [Debugging][30] functionality
                            - side notes:
                                - requires [IPyKernel 6+][46]
                                - debugging cells in a Jupyter Notebook does not make use of [launch configurations][146] --> instead it must be customized via [Settings][12] (e.g.jupyter.debugJustMyCode)
                    - overflow-menu (left to the cell output):
                        - Add Cell Output to Chat
                            - i.e. [GitHub Copilot][172] feature
                        - Clear Cell Outputs
                            - code example:
                                - ```python
                                    for i in range(5):
                                        print(i)
                                    ```
                                - create two cells
                                - in contrast to "Clear All Outputs"-command in the notebook toolbar, this command only clears the output of the respective cell
                        - Copy Cell Output
                    - cell status bar:
                        - provides information about:
                            - current state of the cell:
                                - pending --> circle-arrow with clock symbol
                                - executing --> circling arrows
                                    - code example:
                                        - cell 1:
                                            - ```python
                                                import time
                                                
                                                for i in range(50):
                                                    time.sleep(1)
                                                ```
                                        - cell 2:
                                            - ```python
                                                print("hello world")
                                                ```
                                        - run both cells
                                - execution failed --> red x
                                    - continuing from the previous code example:
                                        - stop cell 1
                                - execution successful --> green checkmark
                                    - continuing from the previous code example:
                                        - run cell 2
                            - current/final run time of the cell
                                - code example:
                                    - ```python
                                        import time
                                        
                                        for i in range(5):
                                            print(i)
                                            time.sleep(1)
                                        ```
                        - language picker:
                            - switch between code cells and Markdown cells 
                            - side note:
                                - switching to a programming language that is different from the kernel:
                                    - language editing features (e.g. syntax highlighting, [IntelliSense][155], etc.) work but you can't run the code
                                        - code example:
                                            - ```julia
                                                for i in 0:4
                                                    println(i)
                                                end
                                                ```
                                            - ```python
                                                for i in range(5):
                                                    print(i)
                                                ```
                                            - select Julia-kernel and run Julia code
                                            - paste Python code into a cell and select "Auto Detect" from the language picker --> syntax highlighting and IntelliSense works but you can't run the code
                                            - select Python-kernel and run Python code and Julia code
                                    - Jupyter Notebook alternative: [Polyglot Notebooks][47] --> provide support for multi-language notebooks
                - Markdown cells:
                    - cell toolbar:
                        - basically the same as for code cells:
                            - similarities:
                                - Split Cell
                                - overflow menu
                                - Delete Cell
                            - difference:
                                - Run Cells in Section
                                    - only works for headings --> [code example][61]
                                - Edit Cell --> Stop Editing Cell*
                                    - *:
                                        - i.e. render the Markdown
                                    - code example:
                                        - create a heading called "Heading"
                                    - side note:
                                        - using respective keyboard shortcuts (Enter and Esc) is more convenient
                    - cell status bar:
                        - in contrast to code cells, there is only the [language picker][77] 
                    - side notes:
                        - collapse/expand-arrow (left to the cell):
                            - only available for headings --> collapses/expands all cells up until the next heading of the same level
                                - [code example][61]
                        - table of contents:
                            - available via the [outline view][166]:
                                - click an outline-entry for quick navigation
                                    - [code example][61]
                                - double-click an outline-entry to jump into the notebook
                            - toolbar when hovering over an outline-entry:
                                - Run Cells in Section
                                - overflow menu --> Fold Section
                            - by default, the outline view only shows Markdown --> enable depiction of code cells* via [Settings][12]: notebook.outline.showCodeCells
                                - *: the first line of the code
                - side notes:
                    - interaction with cells:
                        - collapse/expand cell or cell output:
                            - click vertical bar left to cell or cell output --> or double-click in the area left to cell or cell output
                                - code example:
                                    - ```python
                                        for i in range(5):
                                            print(i)
                                        ```
                        - select multiple cells:
                            - to select consecutive cells:
                                - select a cell --> hold Shift and click the last cell you want to select
                            - to select any group of cells:
                                - hold Ctrl --> click the cells you'd like to add to your selection
                        - move cell:
                            - via drag-and-drop --> drag-and-drop-area is to the left of the cell or cell output*
                                - *: for rendered Markdown cells you can click anywhere
                            - also works when multiple cells are selected
                    - working with plots:
                        - code example:
                            - ```python
                                import matplotlib.pyplot as plt
                                
                                x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                y_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
                                
                                plt.plot(x_values, y_values, marker='o')
                                plt.xlabel("x")
                                plt.ylabel("y")
                                ```
                        - toolbar:
                            - Copy to Clipboard
                            - Expand image:
                                - opens plot viewer --> toolbar:
                                    - arrows: cycle through plots* --> or click respective plot
                                        - *: when multiple plots are opened in the plot viewer
                                    - pan
                                    - zoom in/out --> or via mouse wheel
                                    - save as PDF, PNG or SVG
                                    - trash can symbol: remove plot from plot viewer
                            - Save as*
                                - *: only PNG
                    - search within notebook:
                        - [same functionality][123] as with regular source code files
                        - one additional search option:
                            - Find Filters --> specify across which components of the notebook you want to search:
                                - Markdown Source
                                    - example:
                                        - use "print("hello world")" in all 4 locations --> search for "hello"
                                - Rendered Markdown
                                - Code Cell Source
                                - Code Cell Output
                    - notebook diff editor:
                        - basically [the same functionality][133] as with regular source code files
                            - code example:
                                - copy [notebook_1][62] and [notebook_2][63] --> run those notebooks
                                - right-click "notebook_1" in [Explorer][14] --> "Select for Compare"
                                - right-click "notebook_2" in [Explorer][14] --> "Compare with Selected"
                        - additional features:
                            - 3 categories of diffs:
                                - cell input
                                - cell output
                                - metadata
                            - editor toolbar:
                                - Open Text Diff Editor:
                                    - opens the [diff editor][133] for the underlying JSON files*
                                        - *: since Jupyter Notebooks are [JSON files][49] under the hood
                                    - differences:
                                        - left side = editable; right side = editable
                                        - additional options in editor toolbar:
                                            - Disable wrapping for this file
                                                - code example:
                                                    - after applying this option, the image-diff only takes up one (long) line instead of many (short) lines
                                            - Swap Left and Right Side
                                - overflow menu:
                                    - toggle Metadata diffs and/or Output diffs
                            - diff toolbar:
                                - pilcrow-icon: toggle for showing leading/trailing whitespace diffs in the inputs
                                - Switch Output Rendering:
                                    - switch between rendered output and plain text output --> i.e. display changes as a whole vs display individual changes
                                    - examples:
                                        - rendered plot vs underlying JSON file
                                            - code example:
                                                - see diff of cell 3
                                        - printed output vs actual numbers
                                            - code example:
                                                - see diff of cell 4
                                - Revert Metadata/Inputs/Outputs*
                                    - *:
                                        - peculiarity: outputs don't update automatically in the notebook diff editor --> open another editor and then go back to the diff editor and look at the outputs
                        - difference:
                            - right side = editable
            - Python Interactive Window:
                - purpose:
                    - (like the name implies) to write and run Python code interactively --> i.e. it's similar to the [Python REPL][50]
                - open:
                    - as a standalone console:
                        - [Command Palette][120] --> "Jupyter: Create Interactive Window"
                    - with a file:
                        - [Command Palette][120] --> "Run Current File in Python Interactive Window"
                            - code example:
                                - ```python
                                    for i in range(5):
                                        print(i)
                                    ```
                        - dropdown-menu of [play-button][73]
                - basic usage:
                    - type code into the input box (at the bottom) --> press Enter:
                        - once --> go to a new line
                            - code example:
                                - ```python
                                    for i in range(5):
                                        print(i)
                                    ```
                        - twice* --> execute code
                            - *:
                                - alternatives:
                                    - press play button left to the input box
                                    - change to Shift+Enter via [Settings][12]: interactiveWindow.executeWithShiftEnter
                    - results are shown in notebook-like cells with inputs and outputs
                    - side notes:
                        - [IntelliSense][155] is available
                            -  e.g. member lists, tab completion, quick info/parameter hints
                            - code example:
                                - ```python
                                    import random
                                    ```
                                - ```python
                                    random.randint()
                                    ```
                        - you can re-run cells* --> but you can't modify the code
                            - *:
                                - put cursor into cell and press Shift+Enter
                            - code example:
                                - ```python
                                    lst = []
                                    ```
                                - ```python
                                    lst.append(1)
                                    lst
                                    ```
                                - re-run the first cell and then print out "lst" again
                        - UpArrow/DownArrow: cycle through command history
                - toolbars:
                    - interactive window:
                        - Interrupt
                            - code example:
                                - ```python
                                    import time
                                    
                                    for i in range(10):
                                        print(i)
                                        time.sleep(1)
                                ```
                        - Clear All
                            - clears the cell inputs and outputs 
                        - Restart
                            - restarts the kernel --> i.e. clears the state of the Interactive Window
                            - continuing from the previous code example:
                                - print out "i"
                                - restart the kernel
                                - print out "i" again
                        - Variables
                            - opens [Jupyter-view][162]
                        - Save
                            - exports current cells in the Interactive window as a Jupyter Notebook
                        - Export
                            - exports current cells in the Interactive window as a [Python script][161], HTML file or PDF file
                        - Expand/Collapse
                            - expands/collapses cell inputs
                                - code examples:
                                    - ```python
                                        def some_function():
                                            x = 1
                                            y = 2
                                            z = 3
                                            
                                            return x + y + z
                                        ```
                                    - ```python
                                        for i in range(5):
                                            print(i)
                                        ```
                            - side note:
                                - you can [manually expand/collapse][72] individual cell inputs or outputs
                    - code cell:
                        - Copy Cell*
                            - *: overflow menu left to code output:
                                - Add Cell Output to Chat
                                    - i.e. [GitHub Copilot][172] features
                                - Copy Output
                        - Go to code
                            - if code cell is from a file
                            - code example:
                                - ```python
                                    for i in range(5):
                                        print(i)
                                    ```
                                - put this code into a Python file and run the file in the Interactive Window
                        - Delete Cell
                - side notes:
                    - kernel picker (in the top right corner):
                        - select a kernel/environment
                    - working with plots:
                        - works the same as with [Jupyter Notebooks][167]
                    - executing a selection of code in a Python file:
                        - when pressing Shift+Enter to [execute a code selection][16], you can send the code to the Interactive Window (instead of sending it to the Python REPL in the terminal)
                        - [Settings][12]: jupyter.interactiveWindow.textEditor.executeSelection
                    - Jupyter-like cells within Python files:
                        - how to create:
                            - code cell: "# %%"-comment
                                - code example:
                                    - ```python
                                        # %%
                                        1 + 1
                                        ```
                            - markdown cell: "# %% [markdown]"-comment
                                - code example:
                                    - ```python
                                        # %% [markdown]
                                        # # heading
                                        # - item 1
                                        # - item 2
                                        # - item 3
                                        ```
                                    - gets rendered in the interactive window --> you are probably better off using regular Jupyter Notebooks
                        - cell [CodeLenses][52]:
                            - Run Cell:
                                - runs cell in the Interactive Window --> if it is the last cell in the file, then a new cell is created automatically below
                                - side note:
                                    - keyboard shortcuts:
                                        - Shift+Enter:
                                            - runs the cell* and cursor jumps to the next cell
                                                - *: if it is the last cell in the file, then a new cell is created automatically below
                                        - Ctrl+Enter:
                                            - runs the cell and cursor stays in the cell
                            - Run Below/Above:
                                - Below: only available for the first cell --> runs the respective cell and all cells below it
                                - Above: runs all the cells above the respective cell (but not the respective cell itself)
                            - Debug Cell:
                                - starts the [debugger][30] for the respective cell (and only for the respective cell)
                                    - code example:
                                        - ```python
                                            for i in range(5):
                                                print(i)
                                            ```
                                        - add a breakpoint to this cell and to another cell
                        - side notes:
                            - exporting to a Jupyter notebook:
                                - [Command Palette][120]:
                                    - "Jupyter: Export Current Python File as Jupyter Notebook"
                                    - "Jupyter: Export Current Python File and Output as Jupyter Notebook"
                            - [keyboard shortcuts][131]
                            - code example to demonstrate a potential workflow:
                                - task: reverse the order of the words in a string --> e.g. transform "this is some text" into "text some is this
                                - ```python
                                    # %%
                                    text = "this is some text"
                                    
                                    print(text[::-1]) # doesn't work
                                    
                                    words = text.split()
                                    words_reversed = words[::-1]
                                    text_reversed = " ".join(words_reversed)
                                    ```
            - extension pack:
                - Jupyter Keymap:
                    - provides keyboard shortcuts to match the keybindings from [Jupyter Notebooks][15] --> however: doesn't include all of the keybindings
                    - see list of available commands via [Keyboard Shortcuts Editor][53]:
                        - filter for "Jupyter Keymap"
                        - useful commands (imo):
                            - S: save file
                            - C: copy cell
                            - V: paste cell
                            - X: cut cell
                            - Z: undo
                            - A: insert cell above
                            - B: insert cell below
                            - L: toggle line numbers --> Shift+L: toggle line numbers for all cells
                            - Shift+Enter: execute cell and focus next cell --> jumps to command mode
                            - Ctrl+Enter: execute cell and focus current cell --> jumps to command mode
                            - Ctrl+Alt+Enter: execute cell and focus current cell --> stays in whatever mode you were in
                        - side note:
                            - two other sources for keyboard shortcuts:
                                - System:
                                    - filter for "system" and check only the entries in column "Command" that start with "Notebook"
                                    - useful commands (imo):
                                        - Enter: enter edit mode
                                        - Esc: exit edit mode (i.e. go back to command mode)
                                        - Y: change cell to code cell(s)
                                        - M: change cell to Markdown cell(s)
                                        - Ctrl+#: comment out selected cell(s)
                                        - Shift+UpArrow/DownArrow: expand selection of cell(s)*
                                            - *: consecutive cells or any group of cells
                                        - Alt+DownArrow/UpArrow: move cell(s) down/up
                                        - LeftArrow/RightArrow: fold/unfold Markdown heading
                                - Jupyter extension:
                                    - filter for "jupyter"
                                    - the commands are somewhat inconvenient/cumbersome
                - Jupyter Cell Tags:
                    - purpose:
                        - organization/documentation:
                            - cell tags provide additional context or information --> e.g. function or purpose of a cell
                                - code example:
                                    - ```python
                                        def generate(data):
                                            pass
                                        
                                        def preprocess(data):
                                            pass
                                        ```
                                    - add cell tag "helper functions"
                            - imo: Markdown headings are probably better suited for this purpose
                        - workflow automation:
                            - for example with tools like:
                                - [papermill][54]
                                - [nbconvert][55]
                                - [nbgrader][56]
                    - how to create:
                        - cell toolbar > overflow menu:
                            - Add Cell Tag
                            - Edit Cell Tags (JSON)
                            - Mark Cell as Parameters
                                - code example:
                                    - ```python
                                        x = 1
                                        y = 2
                                        z = 3
                                        ```
                        - cell status bar (after first tag is created):
                            - "+"-button: add tag
                            - "x"-button: remove tag
                    - side note:
                        - Cell Tags-view:
                            - where: in the [Jupyter-view][162]
                            - shows the tags of selected cell (i.e. not the tags of the whole notebook)
                - Jupyter Slide Show:
                    - purpose: create a slide show* out of a Jupyter Notebook
                        - *: based on the [reveal.js framework][57]
                    - how-to:
                        - set up the slides:
                            - cell toolbar > overflow menu:
                                - Switch Slide Type:
                                    - slide
                                    - subslide
                                    - fragment
                                    - skip
                                    - notes
                                    - none
                                        - i.e. removes a created slide-marker again
                                - Edit Slide Type (JSON) --> alternative: click "Slide Type:" in the cell status bar
                            - side notes:
                                - content of a slide:
                                    - the cell with a slide-marker + every cell up until the next cell with a slide-marker
                                - example notebook:
                                    - [without slide markers][102]
                                    - [with slide markers][58]
                        - create the slide show file:
                            - terminal: jupyter nbconvert <file-name>.ipynb --to slides
                        - present the slide show:
                            - [example slide show][103]
                            - navigation: arrows in the bottom-right corner --> or Arrow-keys
                            - press "?" to open a list of available keyboard shortcuts --> e.g.:
                                - S: open "Speaker View"
                                - F: full screen
                                - Esc or O: toggle "Slide Overview"
            - side notes:
                - you can use [magic commands][59]
                    - code example:
                        - ```python
                            %%timeit
                            
                            for i in range(1000):
                                for j in range(1000):
                                    x = i + j
                            ```
                - you can [connect to a remote Jupyter server][60] to offload intensive computation
        - #
        - purpose of extensions:
            - VS Code is a small download* by design and therefore only includes the minimum number of components to accommodate most development workflows --> e.g.:
                - *:
                    - [less than 200MB --> disk footprint: less than 500MB][228]
                - basic functionality like an editor, file management, window management or preference settings
                - built-in support for JavaScript, TypeScript, Node.js, HTML and CSS
            - extension enable you to easily add additional functionality in order to accommodate your specific development workflow --> e.g.:
                - programming languages --> Python, Java, Go, C++, etc.
                    - side note:
                        - (usually) it is not enough to just install the extension of a specific language --> you need to install the language itself
                            - examples:
                                - to use the [Python extension][32] you need to install Python, for example, via [Python.org][33] or via [Anaconda][34]
                                - to use the [Julia extension][35] you need to install [Julia][36]
                - debugging
                - linting
                - formatting
                - version control
                - code completion
                - refactoring
                - code navigation
                - spell-checking
                - [virtual pets][37]
        - searching extensions:
            - type what you are looking for into the search box --> list of search results:
                - search example:
                    - search for "c++"
                - provided info for each search result:
                    - name of the extension
                    - short description
                    - publisher
                    - number of downloads
                    - rating (1 - 5 stars)
                    - install button
            - click on a search result to open the extension's "details page":
                - i.e. the README
                    - example:
                        - click "C/C++ Runner" by "franneck94"
                - additional sub-pages:
                    - features
                        - i.e.: a list of features that the extension adds to VS Code
                        - e.g.: commands, settings etc.
                    - changelog
                    - dependencies (if any)
                - side notes:
                    - additional useful information on the right-hand side of the details page:
                        - unique identifier
                        - current version
                    - click the name to open the marketplace page of the extension
            - side notes:
                - "Extension Packs":
                    - bundle separate extensions together so they can be easily installed at one time
                        - example: "C/C++ Extension Pack"
                    - indicator: small number in the bottom left of the extension logo
                - search options:
                    - clear search results
                    - filter:
                        - various filter options
                            - examples:
                                - featured
                                - recommended
                                    - you can create a recommended list of extensions for a workspace --> ensures that everybody that wants to use the workspace has the same set-up
                                    - [Command Palette][120]: "Configure Recommended Extensions (Workspace Folder)" --> add an extension via [IntelliSense][155] e.g. "ms-python.python"
                                    - the "extensions.json" file is saved into {workspace folder}/.vscode
                                - category --> e.g. data science
                                - enabled/disabled
                        - "sort by"-functionality
                            - example: search for "c++" --> sort by "install count"
                        - side note:
                            - alternatively you can also manually type in the @-sign into the search box
        - managing extensions:
            - install/uninstall:
                - via details page or "install"/"Manage"-gear button in the side bar
                - side note:
                    - once an extension is installed, you can also install a specific version of the extension via the details page or "Manage"-gear button
            - enable/disable:
                - via details page or "Manage"-gear button in the side bar
            - update:
                - VS Code automatically checks for updates and installs them accordingly --> disable auto update for a specific extension via respective "Manage"-gear button
        - side notes:
            - the different views:
                - list the respective extensions based on certain criteria --> installed, recommended, enabled and disabled
            - toolbar:
                - refresh
                - overflow menu:
                    - toggle the different views on/off
                    - disable autoupdate for all extensions --> (manually) check for extension updates
                    - disable/enable all extensions
            - measures undertaken by the [Visual Studio Code Marketplace][99] to protect users against malicious extensions*:
                - *:
                    - they are necessary because the [extension host][98], which is responsible for running extensions, has the same permissions as VS Code itself --> i.e. [malicious code could be automatically executed in the background][230]
                - mechanisms to prevent malicious extensions from being published in the first place:
                    - malware scanning
                        - a malware scan is run (using several antivirus engines) for each new extension and for each extension update --> until the scan is all clear, the extension won't be published
                    - dynamic detection
                        - the extension's runtime behavior is verified by running it in a sandbox environment
                    - unusual usage monitoring
                        - downloads and usage patterns of extensions are monitored to detect unusual behavior
                    - name squatting prevention
                        - prevents extension authors from stealing the names of official publishers (e.g. Microsoft) and popular extensions (e.g. GitHub Copilot)
                    - block List
                        - if a malicious extension is reported and verified, or a vulnerability is found, then the extension is:
                            - removed from the Marketplace
                            - added to a block list --> i.e. if the extension has been installed, it's automatically uninstalled by VS Code
                    - extension signature verification
                        - the Marketplace signs all extensions when they're published --> VS Code checks this signature when you install an extension to verify the integrity and the source of the extension package
                - mechanisms to help users make more informed decisions about already published extensions:
                    - Ratings & Reviews
                        - read what others think about the extension
                    - Q&A
                        - review existing questions and the level of the publisher's responsiveness
                    - links to resources --> e.g. support, issues, repository, etc.
                    - verified publisher badge
                        - blue check mark next to the publisher's name and domain name --> indicates that the publisher has proven domain-name ownership to the Marketplace and the good standing of the publisher on the Marketplace for at least six months
                - side notes:
                    - reporting suspicious extensions:
                        - open the extension's page in the Visual Studio Marketplace
                        - select the "Report a concern"-link at the bottom of the "More Info"-section
                    - as of VS Code release 1.97, when you first install an extension from a third-party publisher, VS Code shows a dialog prompting you to confirm that you trust the extension publisher
                        - example: kaiwood.indentation-level-movement
    - #
    - vertical bar at the left-hand side
    - provides auxiliary functionality that you (typically) need when editing code:
        - by default --> Explorer, Search, Source Control, Debugger and Extensions
        - extensions can add additional functionality --> e.g. the [Python][32] extension adds "Testing"
    - click an icon: toggle side bar --> contains available views and/or features for each respective functionality
    - side notes:
        - Accounts-icon:
            - lets you sign-in into or sign-out of various accounts --> e.g. to [Backup and Sync Settings][229]
                - example: click "Backup and Sync Settings" --> click  "Sign in"
        - Manage-icon:
            - provides general functionality --> e.g.:
                - opening the [Command Palette][120], [Settings][12], [Keyboard Shortcuts][126], etc.
                - adjusting [themes][24]
                - checking for updates
        - icons can display context-specific info
            - examples:
                - Explorer       --> number of unsaved files
                    - code example:
                        - copy and open [this folder][110] --> make changes to two separate files
                - Source Control --> number of pending changes
                    - code example:
                        - copy and open [this folder][87] --> make changes to two separate files
                - Debugger       --> number of [debugger sessions][174]
        - search within views*:
            - *:
                - expand/collapse a view by clicking its name
            - how to access:
                - click into the respective view and press Ctrl+Alt+F
                    - search examples:
                        - Folders-view of the [Explorer][14]:
                            - search for "no"
                            - results are highlighted --> if they are within a folder, then a number next to the folder indicates how many files within that folder match the search criteria
                            - toggle Fuzzy Match off and Filter on
                        - [Outline-view][166]:
                            - search for "bar" in this Markdown file
                        - [Variables-view][198]:
                            - set a breakpoint at line 38 in [this file][91]
                            - run the debugger
                            - you can search for expressions (e.g."element") and values (e.g "3")
                            - side note:
                                - "Filter" only applies to variables that don't contain any "special variables"
                                    - search for "9" and toggle filter on --> only variable "element" gets filtered out and not "lst" or "instance"
            - search options:
                - Filter --> toggle between highlighting or filtering
                - Fuzzy Match --> toggle between fuzzy search or exact search
- # Editor
    - modifying the editor layout:
        - full screen:
            - toggle via:
                - [layout controls][203]
                - [Menu Bar][71]: View > Appearance > Full Screen
                - [Command Palette][120]: "View: Toggle Full Screen"
            - in contrast to maximizing the window, full screen modes hides the [Menu Bar][71] and the buttons to minimize/maximize/close window as well as the Windows Taskbar
        - zen mode:
            - toggle via:
                - [layout controls][203]
                - [Menu Bar][71]: View > Appearance > Zen Mode
                - [Command Palette][120]: "View: Toggle Zen Mode"
                - side note:
                    - you can also exit by double-pressing Esc
            - enables a more minimal editor experience:
                - it basically hides everything of the user interface except the files you are currently working on --> but all the functionality is still available (e.g. via [Command Palette][120])
                - adjust what is being hidden via [Settings][12] --> search for "Zen Mode"
        - centered layout:
            - applies when there is only one editor group
            - toggle via:
                - [layout controls][203]
                - [Menu Bar][71]: View > Appearance > Centered Layout 
                - [Command Palette][120]: "View: Toggle Centered Layout"
            - hold Alt to move the [sashes][206] independently of each other
        - multiple editor groups:
            - different ways of creating a grid layout:
                - drag-and-drop:
                    - the tab of editor A into the left/right/top/bottom half of editor B: splits editor A to the left/right/top/bottom
                    - the tab of editor A into the center of editor B: adds editor A to the editor group of editor B
                    - side notes:
                        - to move a whole editor group, drag-and-drop its title area
                        - drag editor A into editor B while holding Shift: inserts a link to the file of editor A into editor B --> drop-down with different insert options (if available)
                            - example:
                                - drag some file into a Markdown file
                - "Split Editor"-button in Editor toolbar:
                    - splits active editor to the right --> hold Shift or Alt to split to the bottom
                    - example use case: working in different locations of a long file --> i.e. no need for scrolling back and forth
                    - side note:
                        - you can also split the editor within the same editor group:
                            - [Command Palette][120]:
                                - "View: Toggle Split Editor in Group"
                                - "View: Toggle Layout of Split Editor in Group"
                                - "View: Focus Other Side in Active Editor"
                - [Menu Bar][71]: View > Editor Layout:
                    - Split Up/Down/Left/Right
                    - Split in Group
                    - list of predefined grid layouts --> creates empty editor groups* and you can populate them with your files
                        - *:
                            - click "x" in the editor toolbar to close an empty editor group again
                        - side note:
                            - in a 2x2-grid, you can drag the "mid-point" to resize all the windows at the same time
                    - Flip Layout
            - side note:
                - [Settings][12]: workbench.editor.closeEmptyGroups
                    - enabled: empty groups automatically close
                    - disabled: empty groups remain part of the grid
        - side note:
            - floating editor windows:
                - how to create:
                    - [Command Palette][120]:
                        - "Move Editor into New Window"
                        - "Copy Editor Group into New Window"
                    - [Menu Bar][71]: View > Editor Layout:
                        - Move Editor into New Window
                        - Copy Editor into New Window
                    - context menu of the tab:
                        - Move into New Window
                        - Copy into New Window
                    - drag the editor tab out of the current VS Code window and drop it anywhere on your screen*
                        - *: you can also drag it back again into VS Code
                - example purpose:
                    - to move the editor to another place on your monitor or to another monitor
    - code editing:
        - IntelliSense*:
            - *:
                - VS Code's term for code completion features
            - member lists:
                - as you type, a list of possible completions pops up:
                    - code example:
                        - ```python
                            customer_address = "some street"
                            
                            a
                            ```
                    - different [symbols][3] at the front indicate different types of completions --> e.g. keywords, functions, classes, variables etc.
                    - listed options (in order):
                        - options that start with the respective character
                        - options where a sub-section* starts with the respective character
                            - *: sub-sections can be delimited by, for example, an underscore or via CamelCase
                - if you continue typing characters, the list of possible completions is filtered down:
                    - code example:
                        - ```python
                            customer_address = "some street"
                            
                            as
                            aso
                            ```
                    - listed options:
                        - options that match the exact sequence --> either at the beginning or at the start of a sub-section
                        - options that contain the individual characters in the given order*
                            - *:
                                - i.e. the characters don't match the exact sequence
                                - e.g. when going from "as" to "aso" the listed options still contain "AssertionError" and "StopAsyncIteration" but not "customer_address" (because the "o" appears before the "a" and "s")
                - press Tab or Enter to insert the selected option
                - side notes:
                    - member lists also:
                        - support CamelCase-filtering
                            - code example:
                                - ```python
                                    A
                                    ```
                        - work with dot-notation:
                            - modules --> lists contain for example sub-modules, classes or functions
                                - code example:
                                    - ```python
                                        import asyncio
                                        
                                        asyncio.
                                        asyncio.base_events.
                                        ```
                            - classes --> lists contain for example attributes or methods
                                - code example:
                                    - ```python
                                        numbers = [1, 2, 3]
                                        numbers.
                                        
                                        for number in numbers:
                                            number.
                                        ```
                        - show the available parameters of a function
                            - code example:
                                - ```python
                                    print()
                                    ```
                                - put cursor within the parentheses and [manually trigger][208] the member list
                    - IntelliSense provides "intelligent" suggestions:
                        - member lists are not strictly grouped by type-of-completion or ordered alphabetically
                        - instead IntelliSense lists suggestions first that it thinks are most relevant based on different criteria* --> e.g. what you have recently used
                            - *:
                                - behavior can be adjusted via [Settings][12]:
                                    - editor.suggest.localityBonus
                                    - editor.suggestSelection
                        - IMO: this can be confusing sometimes because the order might be different to what you expected --> i.e. it's something to be aware of
                            - code example:
                                - ```python
                                    a
                                    ascii
                                    a
                                    assert
                                    a
                                    ```
            - quick info; parameter hints:
                - how to access:
                    - quick info: hover over entry in member list and click arrow
                        - code example:
                            - ```python
                                import random
                                
                                random.sample
                                ```
                    - parameter hints: when opening the parentheses to call a function/class
                        - continuing from the previous code example:
                            - ```python
                                random.sample()
                                ```
                - similarities:
                    - both depict the available parameters and the docstring 
                - differences:
                    - quick info is more readable:
                        - parameters have syntax highlighting + better formatting
                        - [resizable][206] height and width
                    - parameter hints highlight currently "selected" parameter in blue
                        - continuing from the previous code example:
                            - ```python
                                random.sample([1, 2, 3], )
                                ```
            - tab completion:
                - code example:
                    - ```python
                        very_long_variable_name_1 = 1
                        very_long_variable_name_2 = 2
                        very_long_variable_name_3 = 3
                        
                        very
                    ```
                - by default, tab completion is disabled --> enable it via [Settings][12]: editor.tabCompletion
                - cycle through options by repeatedly pressing Tab
            - tooltips:
                - hover over variables, functions, classes or modules to see the respective tooltip
                    - code example:
                        - ```python
                            lst = [1, 2, 3]
                            for i in lst:
                                print(i)
                            
                            import random
                            x = random.Random()
                            ```
            - side note:
                - the automatic popups can be turned off:
                    - [Settings][12] > Text Editor > Suggestions --> e.g.:
                        - quick suggestions
                            - code example:
                                - ```python
                                    pr
                                    ```
                        - parameter hints
                            - code example:
                                - ```python
                                    print()
                                    ```
                        - suggest on trigger characters
                            - code example:
                                - ```python
                                    lst = [1, 2, 3]
                                    lst.
                                    ```
                        - editor hover
                            - code example:
                                - ```python
                                    lst = [1, 2, 3]
                                    ```
                    - use the [respective keyboard shortcuts][208] to manually trigger IntelliSense
        - Code Actions:
            - indicated via a lightbulb --> it's shown when a code action is available at the current cursor position or for the current selection
                - code example:
                    - ```python
                        sample()
                        
                        some_variable = pow(5, 2)
                        
                        for i in range(10):
                            print(i)
                        ```
                    - cursor on "sample" --> code action
                    - cursor on "some_variable" --> code action
                    - cursor on "pow" --> no code action
                    - select whole for-loop --> code action
                    - select part of for-loop --> no code action
            - click lightbulb to see available code action(s) --> two different types:
                - quick fixes
                    - code examples:
                        - ```python
                            import math
                            
                            sample()
                            
                            variable = "hello worlt"
                            ```
                        - cursor on "math"
                        - cursor on "sample"
                        - cursor on "worlt"*
                            - *: a spellchecker extension is needed for this example
                - refactorings:
                    - extract method
                        - code example:
                            - before
                                - ```python
                                    lst = [1, 2, 3]
                                    
                                    new_list = []
                                    for number in lst:
                                        new_list.append(number + 1)
                                    ```
                            - after
                                - ```python
                                    lst = [1, 2, 3]
                                    
                                    def add_one(lst):
                                        new_list = []
                                        for number in lst:
                                            new_list.append(number + 1)
                                    
                                        return new_list
                                    
                                    new_list = add_one(lst)
                                    ```
                    - extract variable
                        - code example:
                            - before
                                - ```python
                                    round(1000 * pow(1.05, 10))
                                    ```
                            - after
                                - ```python
                                    investment_result = 1000 * pow(1.05, 10)
                                    round(investment_result)
                                    ```
                    - move symbol
                        - code example:
                            - before
                                - ```python
                                    user = "John"
                                    key = "a*4Qv"
                                    
                                    log_in(user, key)
                                    ```
                                - put cursor on "user" --> "Move symbol to new file"
                                - put cursor on "key" --> "Move symbol to..."
                            - after
                                - ```python
                                    from user import key, user
                                    
                                    log_in(user, key)
                                    ```
                    - side notes:
                        - rename symbol
                            - how:
                                - right-click the symbol --> "Rename Symbol"
                            - continuing from the previous code example:
                                - rename "user" to "user_name" --> it doesn't matter in which file you rename the symbol
                                - renaming of symbols also affects file names
                                    - before
                                        - ```python
                                            from user import key, user_name
                                            
                                            log_in(user_name, key)
                                            ```
                                    - after
                                        - ```python
                                            from config import key, user_name
                                            
                                            log_in(user_name, key)
                                            ```
                        - refactor preview:
                            - how: Ctrl+Enter --> opens Refactor Preview in the [Panel][10]
                                - continuing from the previous code example:
                                    - rename "user_name" to "user" again
                            - click entry to open [diff(s)][181]
                            - you can toggle individual changes on/off
            - side note:
                - the lightbulb can be turned off via [Settings][12]: editor.lightbulb.enable --> code actions can still be accessed via [respective keyboard shortcut][235]
        - code formatting:
            - VS Code has built-in formatters for JavaScript, TypeScript, JSON, HTML and CSS
            - format actions*:
                - *:
                    - available via context menu or [Command Palette][120]
                - Format Document
                - Format Selection
                    - code example:
                        - ```javascript
                            for (let i = 1; i < 4; i++) {
                            console.log(i);
                            }
                            
                            for (let i = 1; i < 4; i++) {
                            console.log(i);
                            }
                            ```
                        - Format Document
                        - undo formatting
                        - select second for-loop --> Format Selection
                    - side note:
                        - not all formatters support "Format Selection"
            - formatting can also be triggered based on user gestures:
                - adjustable via [Settings][12] --> e.g.:
                    - editor.formatOnSave
                        - code example:
                            - ```javascript
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                ```
                        - note: if autosave is set to "afterDelay", then the file will only be formatted when saved explicitly
                    - editor.formatOnPaste
                        - code example:
                            - ```javascript
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                ```
                        - side note:
                            - not all formatters support Format On Paste:
                                - to do so they must support formatting a selection
                                - workaround: enable "Format On Save" --> paste + save
                    - editor.formatOnType
                        - code example:
                            - ```javascript
                                for (let i=1;i<4;i++) {}
                                ```
            - additional formatters* can be installed via [Extensions][7] --> you need to set a default formatter:
                - *:
                    - i.e. others than the built-in ones
                - setting a default formatter for a specific language:
                    - when multiple formatters are installed and you try to format something, you will be asked to specify a default formatter
                        - code example:
                            - install the extension esbenp.prettier-vscode --> set tab width to 8 via [Settings][12]
                            - ```javascript
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                ```
                            - "Format Document" --> select Prettier as the default formatter
                            - side note:
                                - you can still use the other formatters as well via "Format Document With..." or "Format Selection With..."
                - setting a default formatter for all languages in general:
                    - [Settings][12]: editor.defaultFormatter
                        - code example:
                            - ```typescript
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                ```
                            - ```javascript
                                for (let i = 1; i < 4; i++) {
                                console.log(i);
                                }
                                ```
                            - set the overall default formatter to "TypeScript and JavaScript Language Features"
                            - format the typescript example --> "TypeScript and JavaScript Language Features" is used
                            - format the javascript example --> "Prettier" is used because the default setting for a specific language takes precedence
                - side notes:
                    - changing the default formatter for a specific language:
                        - [Settings][12]: editor.defaultFormatter --> click "Also modified in..."
                            - code example:
                                - ```javascript
                                    for (let i = 1; i < 4; i++) {
                                    console.log(i);
                                    }
                                    ```
                                - set default formatter for JavaScript to "TypeScript and JavaScript Language Features"
                    - deleting an entry for a specific language:
                        - it is only possible via the "settings.json" file
                        - i.e. not via setting the default formatter for the specific language to "None" in the [Settings][12] --> it inherits whatever the overall default formatter is
        - side notes:
            - linting:
                - definition: linting highlights syntactical/stylistic problems in your source code that might lead to errors
                - problems are:
                    - indicated via squiggle lines --> 3 colors: blue (info), yellow (warning) and red (error)
                        - code example:
                            - ```python
                                "hello worlt"
                                
                                some_variable
                                
                                for i in range(3):
                                print(i)
                                ```
                            - a spellchecker extension is needed for the "hello worlt" example
                    - specified:
                        - by rich language services*
                        - by linters*
                        - via configured tasks
                        - *:
                            - adjust if a problem gets treated as an error, warning or info via [Settings][12]
                            - Example for Python:
                                - setting ID: python.analysis.diagnosticSeverityOverrides
                                - click "Edit in settings.json"
                                - set the value for "reportUndefinedVariable" to "error"
                                - "some_variable" in the previous code example gets now treated as an "error" and not a "warning" anymore
                    - side note:
                        - the [Status Bar][156] and [Problems-view][157] provide additional information about problems
                - different linters can be installed via [Extensions][7]:
                    - e.g. for Python: Flake8 or Pylint
                    - run them in parallel or disable/uninstall the linter(s) that you don't use
                        - continuing from the previous code example:
                            - install Flake8 --> [Problems-view][157]: the syntax error is detected by Flake8 and Pylance
                            - disable Flake8 --> the syntax error is only detected by Pylance
            - multiple cursors/selections:
                - add cursor: Alt+Click
                    - code example:
                        - ```python
                            data_base = [
                                {"id": 1, "user": "John"},
                                {"id": 2, "user": "Jane"},
                                {"id": 3, "user": "Bill"}
                            ]
                            ```
                        - add new entry in the middle --> "achievements": None
                - add selection: Alt+Double-Click or Alt+Drag
                    - continuing from the previous code example:
                        - rename "user" to "name"
                - column selection/box selection: Shift+Alt+Click or Shift+Alt+Drag
                    - continuing from the previous code example:
                        - delete entries --> "achievements": None
                        - place cursor in one corner --> hold Shift+Alt while clicking into/dragging to the opposite corner
                - return to one cursor: Esc
                - side notes:
                    - change modifier key for applying multiple cursors to Ctrl:
                        - [Settings][12]: editor.multiCursorModifier
                        - [Menu Bar][71]: Selection > Switch to Ctrl+Click for Multi-Cursor
                    - set column selection as the default behavior (rather than line wrapping selection):
                        - [Settings][12]: editor.columnSelection
                        - [Menu Bar][71]: Selection > Column Selection Mode
                        - side note:
                            - column selection can also be turned off by clicking the "Column Selection"-button in the [Status Bar][9]
            - overtype mode:
                - toggle via [Command Palette][120]: "Toggle Overtype/Insert Mode"
                    - side note:
                        - overtype mode can also be toggled off by clicking the "OVR" indicator in the [Status Bar][9]
                - lets you overwrite existing characters at the cursor position (instead of inserting them)
                    - code example:
                        - ```python
                            def create_user_entry(name, handle, email):
                                """
                                Name        - Full legal name
                                Handle      - Unique public identifier
                                Email       - User's email address
                                """
                                pass
                            ```
                        - rename the parameter "handle" to "user_name" in insert mode
                        - rename "Handle" in the docstring to "User Name" first in insert mode and then in overtype mode
                - related [Settings][12]:
                    - editor.overtypeCursorStyle
                    - editor.overtypeOnPaste
            - different selections via clicking with the mouse:
                - double-click:     selects word
                - triple-click:     selects line
                - quadruple-click:  selects file
    - code navigation:
        - tabs:
            - opened files are depicted via tabs in the title area (i.e. above the editor):
                - two files with the same name open --> location (i.e. folder name) is additionally depicted
                    - example:
                        - create two files with the same name --> put one of them in the root folder of the workspace and the other somewhere two folders deep
                - if more files open than can fit in the title area --> horizontal scrollbar appears
                    - side note:
                        - related [Settings][12]:
                            - workbench.editor.titleScrollbarSizing
                            - workbench.editor.wrapTabs
            - a dot indicates unsaved changes
                - side notes:
                    - dealing with dirty writes:
                        - saving a file that has changed on disk --> VS Code shows error message:
                            - code example:
                                - initial code:
                                    - ```python
                                        print("Hello World!")
                                        
                                        for i in range(10):
                                            print(i)
                                        ```
                                    - open this code in VS Code and in another editor
                                - changes within another editor:
                                    - ```python
                                        print("Hello World!")
                                        
                                        # other editor
                                        
                                        for i in range(10):
                                            print(i)
                                        
                                        # other editor
                                        ```
                                - changes within VS Code:
                                    - ```python
                                        print("Hello World!")
                                        
                                        # VS Code
                                        
                                        for i in range(10):
                                            print(i)
                                        
                                        # VS Code
                                        ```
                                - save changes within the other editor --> save changes within VS Code
                            - Compare --> opens [diff editor][133] to compare new changes with changes on disk
                                - differences:
                                    - two additional buttons:
                                        - check mark: use new changes and discard changes on disk
                                        - curved arrow: discard new changes and use changes on disk
                                    - right side = editable --> e.g. if you want a mix of the new changes and changes on disk
                            - Overwrite --> overwrites the changes on disk
                    - toggle auto save:
                        - [Settings][12]: files.autoSave
                        - [Menu Bar][71]: File > Auto Save
                        - [Command Palette][120]: "File: Toggle Auto Save"
            - actions:
                - click: show respective file in editor --> click the "x" to close it
                - double-click: expand/shrink editor width
                - drag-and-drop: reorder tabs
                - right-click:
                    - Pin: pin tab to beginning
                        - pinned tab stays at the front when scrolling horizontally*
                            - *: peculiarity --> [Settings][12]: workbench.editor.pinnedTabSizing must be set to other setting than "normal"
                        - pinned tab stays open when using "close all" commands:
                            - [Editor toolbar][178]
                            - [open editors-view][130]
                        - unpin: right-click > Unpin --> or clicking the pin-symbol
                        - side note:
                            - [Settings][12]: workbench.editor.pinnedTabsOnSeparateRow
                                - you can pin and unpin editors by dragging and dropping their tabs between the two rows
                    - Close Others
                    - Close to the Right
                - side note:
                    - actions can also be performed on multiple tabs simultaneously:
                        - selecting individual tabs: hold down Ctrl and select respective tabs
                        - selecting a range of tabs: hold down Shift and select the first and last tab in the range
            - other related [Settings][12]:
                - workbench.editor.showTabs
                    - alternative navigation: [open editors-view][192]
                - workbench.editor.openPositioning
                - side note:
                    - [customizing tab labels][195]
        - breadcrumbs:
            - breadcrumbs show the file path and the symbol* path up to the cursor position
                - *:
                    - if the file type has language support for symbols
                - code example:
                    - ```python
                        class Calculator:
                            
                            def add(self, x, y):
                                result = x + y
                                return result
                        ```
                    - add the code to the end of [this file][29]
                    - cursor on empty line --> folder + file
                    - cursor on "result" (in "result = x + y") --> folder + file + symbols
            - clicking a breadcrumb --> opens a dropdown menu for quick navigation:
                - breadcrumb = symbol: dropdown with all available symbols
                - breadcrumb = file/folder: dropdown with all siblings/children
            - related [Settings][12]:
                - Workbench > Breadcrumbs --> e.g. enabled*, file path, symbol path, what elements to show
                    - *: alternatively via [Menu Bar][71] > View > Appearance
        - scrolling:
            - overview ruler:
                - click or drag to quickly navigate file
                - horizontal line: cursor position
                - grey square: (context-specific) occurrences of selected word
                    - code examples:
                        - [file][29]
                        - place cursor on "print" on line 21 --> all occurrences in the file
                        - place cursor on "game_board":
                            - line 25 --> all occurrences in the local scope of the function
                            - line 118 --> all occurrences in the global scope
                - blue/yellow/red square: [info/warning/error][168]
                    - code example:
                        - ```python
                            "hello worlt"
                            
                            some_variable
                            
                            for i in range(3):
                            print(i)
                            ```
                        - a spellchecker extension is needed for the "hello worlt" example
            - minimap:
                - click or drag to quickly navigate file
                - differences to overview ruler:
                    - code is depicted in miniaturized form --> i.e. provides high-level overview of code
                    - cursor position is not depicted
                    - code selection is depicted as a blue block
                - grey line: (context-specific) occurrences of selected word
                    - code examples:
                        - [file][29]
                        - place cursor on "print" (line 21) --> all occurrences in the file
                        - place cursor on "game_board":
                            - line 25 --> all occurrences in the local scope of the function
                            - line 118 --> all occurrences in the global scope
                - blue/yellow/red line: [info/warning/error][168]
                    - code example:
                        - ```python
                            "hello worlt"
                            
                            some_variable
                            
                            for i in range(3):
                            print(i)
                            ```
                        - a spellchecker extension is needed for the "hello worlt" example
                - related [Settings][12]:
                    - Text Editor > Minimap --> e.g. autohide, enabled*, render characters, scale, show slider, side
                        - *: alternatively via [Menu Bar][71] > View > Appearance
            - side notes:
                - fast scrolling:
                    - how to activate*: hold Alt while scrolling
                        - *: also applies to the [Explorer][14]
                    - adjust speed via [Settings][12]: editor.fastScrollSensitivity
                - locked scrolling:
                    - synchronizes scrolling across all visible editors
                        - i.e. when you scroll in one editor, all the other editors scroll by the same amount to keep everything aligned
                    - [Command Palette][120]: "View: Toggle Locked Scrolling Across Editors" --> indicator in [Status Bar][9]
                - sticky scroll:
                    - how to activate:
                        - [Menu Bar][71] > View > Appearance > Sticky Scroll
                        - [Command Palette][120]: "View: Toggle Editor Sticky Scroll"
                        - [Settings][12]: editor.stickyScroll.enabled
                    - sticks the starting line of higher-order scopes* at the top of the editor --> click the element to jump to its respective line
                        - *: based on, for example, [indentation levels][201] or [headings][80]
                    - related [Settings][12]:
                        - editor.stickyScroll.defaultModel
                            - code example:
                                - ```python
                                    class MyClass():
                                        def method(self, x):
                                            for i in range(5):
                                                print(i)
                                                # comment header 1
                                                    # comment header 1.1 ###################################################################
                                                        # comment header 1.1.1
                                                            
                                                            
                                                            
                                                            # comment body
                                                            # comment body
                                                            # comment body
                                    ```
                        - editor.stickyScroll.maxLineCount
                        - editor.stickyScroll.scrollWithEditor
        - search within file:
            - press Ctrl+F to open the Find Widget:
                - if cursor is currently placed on a word, then input box is automatically populated with that word
                    - code examples:
                        - [file][29]
                        - place cursor on empty line
                        - place cursor on "game_board" (line 7)
                    - can be turned off via [Settings][12]: editor.find.seedSearchStringFromSelection
                - search results are highlighted (orange) in the editor, [overview ruler][158] and [minimap][159]
            - search actions:
                - up/down arrow: jump to previous/next match
                - "Find in Selection"-button: search only within selection
                    - continuing from the previous code example:
                        - select the whole "create_initial_game_board" function (lines 4-15)
                        - toggle hamburger icon on/off
                - x: exit the Find Widget --> or press Esc
            - search options:
                - match case
                    - code example:
                        - [file][29] --> search for "Game"
                - match whole word
                    - i.e. it doesn't match when there are letters, numbers or underscores right before or behind the search term
                    - code example:
                        - [file][29] --> search for "game"
                - regular expression
            - replace-functionality:
                - toggle via arrow on the left of the Find Widget
                - actions:
                    - replace (only selected instance)
                        - code example:
                            - [file][29] --> search for "game" and replace with "play"
                    - replace all
                - options:
                    - preserve case
                        - code example:
                            - [file][29] --> search for "game", go to match 43 ("Game finished!!!") and replace all with "play"
            - side notes:
                - use UpArrow/DownArrow keys to scroll through search history
                - multi-line search: Ctrl+Enter
                    - code examples:
                        - [file][29] --> search for "function" on the first line and "def" on the second line --> 0 search results*
                            - *:
                                - the two lines are not treated independently of each other --> i.e. find a place in the file where there is "function" somewhere on one line and then "def" somewhere on the next line
                                - but instead the two lines are more treated like a continuous string --> i.e. find a place where there is "function" followed by a new line beginning with "def"
                        - [file][29] --> search for "function" on the first line and "    def" on the second line --> 1 search result
        - "go to"-functionality --> right-click:
            - go to definition:
                - jumps to the definition of a symbol
                    - code example:
                        - [file][29]
                        - "go to definition" on the function "make_move" (line 129)
                        - "go to definition" on the variable "players" (line 125)
                - if there are multiple definitions, then inline window* opens --> click to preview definition; double-click to jump to definition
                    - code example:
                        - [file][29] --> "go to definition" on "game_status" (line 148)
                    - *:
                        - depicted at the top:
                            - file name
                            - absolute file path
                            - number of definitions
                        - click "x" to close --> or press Esc
                        - you can drag-and-drop an entry into a separate editor
                - also works across files --> especially useful when working with modules/packages
                    - code example:
                        - ```python
                            import random
                            
                            random.sample()
                            ```
                        - "go to definition" on "sample" --> jumps to "sample = _inst.sample" within random.py --> "go to definition" on "sample" in "_inst.sample" --> jumps to actual definition of sample
                        - "go to definition" on "random" --> jumps to random.py
                - side note:
                    - alternatives:
                        - Ctrl+Click:       jumps to definition
                        - Ctrl+Alt+Click:   opens definition to the side
            - go to declaration:
                - jumps to the declaration of a symbol --> for Python it jumps to the respective [.pyi file*][25] (if available)
                    - *:
                        - has something to do with [type checking][26]
                    - code example:
                        - ```python
                            import random
                            
                            random.sample()
                            ```
                        - "go to declaration" on "sample" --> jumps to random.pyi
                - otherwise: the same behavior as "go to definition"
                    - code example:
                        - [file][29] --> "go to declaration" on the function "make_move" (line 129)
            - go to type definition:
                - used with variable: jumps to the definition of the underlying data type (not the definition of the variable):
                    - code example:
                        - ```python
                            class MyClass:
                                
                                def my_method(self):
                                    pass
                            
                            instance = MyClass()
                            
                            instance
                            ```
                        - "go to definition" vs "go to type definition" on "instance"
                - otherwise: same behavior as "go to definition"
                    - code example:
                        - [file][29] --> "go to type definition" on the function "make_move" (line 129)
            - go to implementations:
                - for an interface, this shows all the implementors of that interface
                - for abstract methods, this shows all concrete implementations of that method
                    - code example:
                        - ```python
                            from abc import ABC, abstractmethod
                            
                            # Abstract base class
                            class Animal(ABC):
                                @abstractmethod
                                def speak(self):
                                    pass
                            
                            # Implementation 1
                            class Dog(Animal):
                                def speak(self):
                                    print("Woof!")
                            
                            # Implementation 2
                            class Cat(Animal):
                                def speak(self):
                                    print("Meow!")
                            ```
                        - "go to implementation" vs "go to definition/declaration/type definition/reference" on "speak" on line 6
            - go to references:
                - jumps to the place where the symbol is referenced:
                    - single reference: jumps directly to reference
                        - code example:
                            - [file][29] --> "go to reference" on the function "make_move" (line 39)
                    - multiple references: opens [inline window][177] that shows all references --> click to preview reference; double-click to jump to reference
                        - code example:
                            - [file][29] --> "go to reference" on the function "show" (line 18)
            - side notes:
                - "go to"-functionality is language-specific
                    - i.e. some functionality might not be available for a specific language
                - peeking:
                    - instead of jumping directly to the definition/declaration/type definition/implementation/reference, it opens an [inline window][177] with the definition/declaration/type definition/implementation/reference
                        - code example:
                            - [file][29] --> "go to definition" vs "peek definition" on the function "make_move" (line 129)
        - side notes:
            - folding:
                - hover over the gutter --> shows all foldable regions with a "v":
                    - click "v" to fold
                        - code example:
                            - ```python
                                class MyClass:
                                    
                                    def method_1(self):
                                        for i in range(5):
                                            print(i)
                                    
                                    def method_2(self):
                                        for i in range(5):
                                            print(i)
                                
                                def function():
                                    print("Hello World!")
                                
                                instance = MyClass()
                                function()
                                ```
                    - click ">" to unfold* --> the ">" stays even when not hovering
                        - *: alternatively click the three dots at the end of the line
                - Shift+Click to fold/unfold all regions inside a region
                    - continuing from the previous code example:
                        - Shift+Click "MyClass"
                - side note:
                    - regions can also be:
                        - defined by markers:
                            - specific to each [language][233] --> e.g. Python: #region + #endregion
                                - [code example][29]:
                                    - line 3:   add "#region"
                                    - line 108: add "#endregion"
                            - [minimap][159] depicts the folding marker names
                                - continuing from the previous code example:
                                    - line 3: add "functions" after the "#region" marker
                        - created from selections:
                            - [Command Palette][120]:
                                - "Create Folding Range from Selection"
                                - "Remove Manual Folding Ranges"
            - indent guides:
                - vertical lines that indicate indentation levels --> useful for navigating nested code structures
                    - code example:
                        - [file][29] --> lines 115 - 152
                - currently "active" indent guide gets highlighted
                    - code example:
                        - [file][29]
                        - place cursor on lines 121 or 127 --> you can easily see what code belongs to the respective while-loop
                - side note:
                    - [Settings][12]: editor.guides.indentation
            - bracket pairs:
                - opening and closing parentheses/brackets/braces can be colorized:
                    - [Settings][12]: editor.bracketPairColorization.enabled
                    - code example:
                        - ```python
                            result = (((1 + 2) * 3 + 4) - ((5 + 6) * 7 + 8)) / 9
                            ```
                    - side note:
                        - by default: three different types of colors --> colors can be customized:
                            - click the "Workbench: Color Customizations"-link in the "Bracket Pair Colorization"-setting
                            - click "Edit in settings.json"-link in the "Color Customizations"-setting
                                - code example:
                                    - ```json
                                        "workbench.colorCustomizations": {
                                            "editorBracketHighlight.foreground1": "#4daf4a",
                                            "editorBracketHighlight.foreground2": "#377eb8",
                                            "editorBracketHighlight.foreground3": "#e41a1c"
                                        },
                                        ```
                - guides of opening and closing parentheses/brackets/braces can be colorized:
                    - [Settings][12]:
                        - editor.guides.bracketPairs
                        - editor.guides.bracketPairsHorizontal
                        - editor.guides.highlightActiveBracketPair
                    - code example:
                        - ```python
                            customers = {
                                "id_1": {
                                    "name": "John",
                                    "age": 42,
                                    "ordered_items": [
                                        "hammer",
                                        "nails"
                                    ]
                                },
                                "id_2": {
                                    "name": "Jane",
                                    "age": 35,
                                    "ordered_items": [
                                        "screwdriver",
                                        "screws"
                                    ]
                                }
                            }
                            ```
                        - place cursor on "screws" --> you can easily see everything that belongs to "ordered_items"
                        - place cursor on "age" --> you can easily see everything that belongs to "id_2"
                        - place cursor on "id_2" --> you can easily see everything that belongs to "customers"
            - vertical rulers:
                - add vertical column rulers to the editor via [Settings][12]: editor.rulers
                    - example setting:
                        - "editor.rulers": [20, 40, 60]
    - running code:
        - language-specific functionality --> e.g. Python*:
            - *:
                - other languages may have less/same/more functionality
            - play-button in Editor toolbar:
                - drop-down arrow opens menu with available commands:
                    - "Run Python File":
                        - runs file in the [(integrated) terminal][160]
                        - code example:
                            - ```python
                                for i in range(5):
                                    print(i)
                                ```
                    - "Run Python in Dedicated Terminal":
                        - runs file in a dedicated terminal --> i.e. by executing this command, the file is always run in this specific terminal
                            - code example:
                                - file_1:
                                    - ```python
                                        for i in range(5):
                                            print(i)
                                        ```
                                - file_2:
                                    - ```python
                                        print("Hello World!")
                                        ```
                                - run file 1 in dedicated terminal
                                - run file 2 in dedicated terminal
                                - run file 1 in dedicated terminal
                                - side note:
                                    - command "Run Python File" runs the respective file again in the non-dedicated terminal
                        - example use case:
                            - running a file in the background while doing other things in the non-dedicated terminal
                                - code example:
                                    - file_background:
                                        - ```python
                                            import time
                                            
                                            for i in range(50):
                                                print(i)
                                                time.sleep(1)
                                            ```
                                    - file_1:
                                        - ```python
                                            for i in range(5):
                                                print(i)
                                            ```
                                    - file_2:
                                        - ```python
                                            print("Hello World!")
                                            ```
                                    - run "file_background" in a dedicated terminal
                                    - run files "file_1" and "file_2" in the non-dedicated terminal
                    - "Debug Python File":
                        - starts the [Debugger][30]
                    - "Debug using launch.json"
                        - starts the [Debugger][30] with a [launch configuration][146]
                - side notes:
                    - play-button always executes the latest command that was picked from the dropdown menu --> hover to see currently "active" command
                        - side note:
                            - if latest command was "Debug Python File", then the play-button additionally depicts a bug
                    - "Run Python File"-command is also available via [Command Palette][120] or context menu
            - the Python REPL can be invoked via the [Command Palette][120]:
                - "Start Terminal REPL"
                - "Start Native Python REPL"
                    - provides additional features compared to the classic Python REPL --> e.g. Intellisense, syntax highlighting or "REPL Variables"-view
            - running just a selection/line of code:
                - "Run Selection/Line in Python Terminal"-command is available via [Command Palette][120] or context menu --> opens the Python REPL and runs the selection
                    - code example:
                        - ```python
                            for i in range(5):
                                print(i)
                            
                            for j in range(10):
                                if j > 5:
                                    print(j)
                            ```
                        - select the first for-loop and execute the command
                - side notes:
                    - if you want to use the "Run Python File"-command via the play-button again, then you need to first exit the REPL* --> "exit()" or "quit()"
                        - *: vice versa, if you want to use the "Run Selection/Line"-command again, then you need to open the REPL first OR kill the terminal and open a new one
                    - Smart Send:
                        - if there isn't a selection, Smart Send will send the smallest runnable block of code around the line where the cursor is placed --> after that it places the cursor at the next line of code
                            - continuing from the previous code example:
                                - place the cursor somewhere on the line "for i in range(5):" and execute the command
                                - place the cursor somewhere on the line "print(i)" and execute the command
                                - place the cursor somewhere on the line "print(j)" and execute the command
                        - can be turned off via [Settings][12]: python.REPL.enableREPLSmartSend
                            - continuing from the previous code example:
                                - disable the setting --> place the cursor somewhere on the line "print(j)" and execute the command
                    - the code can also be send to the [Native Python REPL][51]
                        - [Settings][12]: python.REPL.sendToNativeREPL
        - general functionality*:
            - *:
                - i.e. should apply to all languages
            - manually run a file via integrated terminal
                - code example:
                    - ```python
                        print("Hello World!")
                        ```
            - [Command Palette][120]: "Run Active File In Active Terminal" --> file needs [shebang][31]
                - code example:
                    - ```python
                        #!/usr/bin/env python
                        
                        print("Hello World!")
                        ```
                - side note:
                    - runs in the "active" (i.e. currently selected) terminal --> regardless if terminal is a dedicated or non-dedicated terminal
            - [Menu Bar][71]: Run > Run Without Debugging
                - code example:
                    - ```python
                        import time
                        
                        for i in range(50):
                            print(i)
                            time.sleep(1)
                        ```
                    - breakpoints will be ignored --> set breakpoint at line 4
                    - you can restart/stop the program via the debug toolbar
                - side note:
                    - "Run Without Debugging" is always available, but not all debugger extensions support it --> "Run Without Debugging" = "Start Debugging"
    - side notes:
        - Editor toolbar > overflow menu:
            - Show Opened Editors
                - shows opened editors of the active group
            - Close All
                - closes all editors of the active group --> exception: [pinned editors][127]
            - Close Saved
                - closes all saved editors of the active group --> exception: [pinned editors][127]
            - [Enable Preview Editors][124]
            - Maximize Group
            - Lock Group
                - new editors will not open into a locked group*
                    - *: unless explicitly moved there --> e.g. via drag and drop
                - use cases:
                    - if you are working on specific files and don't want them to be replaced while exploring other files
                    - using a [terminal in the editor area][111]
                - click the lock icon in the Editor toolbar to unlock an editor group
                - [Settings][12]: workbench.editor.autoLockGroups
            - Configure Editors
                - opens Editor-related [Settings][12]
        - some customizations:
            - [Menu Bar][71] > View: Word Wrap
                - toggled on: text automatically moves to the next line when it reaches the end of the container
                - toggled off: text stays on a single line causing it to overflow beyond the container --> horizontal scrolling required
            - [Settings][12]:
                - Text Editor > Cursor --> e.g. blinking, style, width
                - Text Editor > Font --> e.g. family, size, weight
                - editor.lineNumbers
                - editor.renderWhitespace
- # Panel
    - an extra space below the [Editor][13] region for additional views --> open/close via:
        - [Layout Controls][199]
        - [Command Palette][120]: e.g. "View: Focus into Panel" or "View: Toggle Panel Visibility"
        - dragging the upper sash
    - default views*:
        - *:
            - in contrast to the views in the [Activity Bar][65], these are typically views that require more horizontal space instead of vertical space --> e.g. [Debug Console][153] vs [Debugging][30]
        - Problems:
            - displays the identified [problems*][168] --> total number of problems (for all opened editors) is depicted next to the heading
                - *:
                    - i.e. errors, warnings or infos
                - code example:
                    - ```python
                        # syntax error
                        for i in range(3):
                        print(i)
                        
                        # undefined function
                        sleep(1)
                        
                        # simple spelling mistake
                        "hello worlt"
                        ```
                    - a spellchecker extension is needed for the "hello worlt" example
                    - paste this code into two separate files
            - problems are ordered by file (tree-view) or by type of problem (table-view):
                - symbols:
                    - red circle with "x" --> error
                    - yellow triangle with "!" --> warning
                    - blue circle with "i" --> info
                - listed details:
                    - actual problem is stated
                    - extension/linter that detected the problem
                    - location of the problem --> line and column number
                - click entry to jump to the respective problem
                - hover over an entry: lightbulb indicates a [quick fix][169] (if available)
            - toolbar:
                - input box to filter the listed problems
                    - search examples:
                        - specific text: e.g. "py" --> shows every problem that somehow contains "py"*
                            - *: regardless of whether "py" appears in the actual stated problem, the file name or the extension that detected the problem
                        - specific files: e.g. "*.py" --> shows only Python files
                    - more filters:
                        - toggle errors/warnings/infos
                        - show active file only
                            - i.e. only shows the problems in the currently active editor and not for all opened editors
                        - show [excluded files][11]
                            - example:
                                - see [Settings][12]: files.exclude --> exclude Markdown files by adding the pattern "**/*.md"
                - collapse all
                - toggle tree-view or table-view
                - maximize/minimize panel and hide panel --> also available for all the other views in the Panel
        - Output:
            - displays status messages and logs from extensions and from VS Code itself* --> useful for troubleshooting issues/bugs
                - *: i.e. lets you investigate the internal operations of extensions and VS Code
            - toolbar:
                - input box to filter the output
                - drop-down list for selecting the output source --> e.g. Git, Python, Tasks, etc.
                - clear output
                - toggle auto scrolling
                - set log level --> ordered from most verbose (Trace) to least verbose (Error)
                    - code example:
                        - set output source to "Python" and the log level to "Trace"
                        - type some code:
                            - ```python
                                lst = [1, 2, 3]
                                for element in lst:
                                    print(element)
                                ```
                - overflow menu:
                    - open output in editor/new window
                    - save output as/export logs
                    - add compound log
                        - lets you create a log from multiple sources --> gets added to the drop-down list*
                            - *: is removed again when VS Code is restarted
                    - import log
                        - i.e. import log from a log file
        - [Debug Console][153]
        - Terminal:
            - provides an integrated terminal* --> opens in the location of the workspace**
                - *: i.e. you can keep working within VS Code and don't have to use an external terminal/command line/shell
                - **: if no workspace is opened, then it opens in the root directory
            - toolbar:
                - name of current terminal:
                    - hover to see additional information
                    - click to open context menu:
                        - move terminal into editor area*/new window
                            - *:
                                - right-click tab: "Move Terminal into Panel"
                            - side note:
                                - you can also drag-and-drop the terminal into the editor area
                        - change color/icon
                        - rename
                        - toggle size to content width
                            - when the terminal width is smaller than the depicted lines --> toggle between:
                                - horizontal scrollbar
                                - depicting line within the given width
                - "+"-sign: add a new terminal --> list of all created terminals on the right-hand side
                    - side note:
                        - drag-and-drop to rearrange the list of terminals
                - drop-down arrow next to the "+"-sign:
                    - select which type of terminal* to add --> e.g. Powershell, bash, etc.
                        - *: available types depend on what shells are installed on your machine
                    - configure terminal settings
                        - *: opens [Settings][12] --> filtered down to settings related to the terminal
                    - select default profile --> i.e. what type of terminal should be created when clicking "+"-sign
                    - run/configure [tasks][5]
                - split terminal
                    - i.e. if you want to depict multiple terminals next to each other in the Terminal-view
                    - side notes:
                        - if multiple terminals are open, then the "split terminal" and "kill terminal" buttons are depicted in the list of terminals on the right-hand side
                        - you can also drag-and-drop a terminal from the list on the right-hand side into the currently active terminal
                        - context menu: unsplit terminal
                - kill terminal
                - overflow menu:
                    - clear terminal
                    - scroll to next/previous command
                        - example command with a lot of output: "git -h"
                    - run active file
                        - code example:
                            - file needs [shebang][31]
                            - ```python
                                #!/usr/bin/env python
                                
                                for i in range(5):
                                    print(i)
                                ```
                    - run selected text
                        - example: git -h
            - side notes:
                - shell integration:
                    - VS Code has the ability to integrate with common shells --> enables additional features
                    - example features:
                        - command decorations*:
                            - *:
                                - dot left to the prompt --> also indicated via the overview ruler
                            - indicate execution status:
                                - grey (hollow) dot: waiting for a command or currently running
                                    - code example:
                                        - ```python
                                            import time
                                            
                                            for i in range(5):
                                                print(i)
                                                time.sleep(1)
                                            ```
                                        - run file from the terminal
                                - blue dot: successful
                                - red dot: failed
                            - hover to see when command was executed and run time of the command
                            - click to show command actions
                            - [Settings][12]: terminal.integrated.shellIntegration.decorationsEnabled
                        - command guide:
                            - vertical bar that shows up beside a command and its output when hovered --> helps to more quickly identify a command
                                - command examples:
                                    - ls
                                    - pwd
                            - [Settings][12]: terminal.integrated.shellIntegration.showCommandGuide
                        - sticky scroll:
                            - enable via [Settings][12]: terminal.integrated.stickyScroll.enabled
                            - sticks the current command at the top of the terminal --> useful for commands with long outputs
                                - example commands:
                                    - git -h
                                    - conda -h
                            - click on the sticky scroll component to scroll to the command's location in the terminal
                - find functionality: Ctrl+F
                    - basically the same as the [find functionality][123] in the Editor
                    - example:
                        - command "git -h" --> search for "work"
                - all text in the terminal output is clickable with Ctrl+Click
                    - useful for opening URLs, files, folders etc. --> for other text, VS Code tries to search the workspace for files that contain the text
                    - code example:
                        - ```python
                            print("https://code.visualstudio.com/docs")
                            print("hello world")
                            ```
                        - open a bash terminal and run the command "ls"
                        - run a Python file with the above code from the terminal
                - [Settings][12]: terminal.integrated.rightClickBehavior
                - advanced topics:
                    - [terminal customization][238]
                    - [terminal profiles][239]
        - Ports:
            - enables [port forwarding][69] --> i.e. when running a local web service, you can use the Ports-view to make the service accessible to others over the internet
    - side note:
        - additional views might be added by [Extensions][7]
            - examples:
                - [Code Spell Checker][70]
                    - adds "Spell Checker" view
                - [Python][32]
                    - when running a test, the "Test Results" view is added
                - [Jupyter][68]
                    - when opening a Jupyter Notebook file, the [Jupyter-view][162] is added
- # Status Bar
    - horizontal bar at the bottom of the window --> different colors based on the specific context:
        - default colors*:
            - *:
                - using the "Dark+" [color theme][170]
            - purple: no workspace opened
            - blue: [workspace opened][136]
            - orange: [currently debugging][207]
        - colors can be [adjusted][170]
    - provides information (and respective functionality) related to the current workspace and/or opened files:
        - [Open a Remote Window][220]
        - Errors/Warnings/Infos:
            - lists the total number of [errors, warnings and infos][168] for all opened editors
                - code example:
                    - ```python
                        # syntax error
                        for i in range(3):
                        print(i)
                        
                        # undefined variable
                        print(value_1)
                        
                        # simple spelling mistake
                        "hello worlt"
                        ```
                    - a spellchecker extension is needed for the "hello worlt" example
            - click to open the [Problems-view][157]
        - Cursor Position:
            - depicts line and column number
            - click to [navigate to a specific line number][66]
        - Indentation Specification:
            - click to change specification:
                - code example:
                    - ```python
                        for i in range(5):
                        ```
                    - press Enter to create indentation with 4 Spaces
                    - select "Indent Using Spaces" --> set tab size to "8" --> press Enter to create indentation with 8 Spaces
                    - [Settings][12]: python.analysis.autoIndent --> needs to be turned off
                - only applies to the currently active file
            - additional options:
                - detect indentation from file
                    - continuing from the previous code example:
                        - manually create an indentation with 6 Spaces and add "print(i)" --> detect indentation
                - convert indentation to spaces/tabs
                    - continuing from the previous code example:
                        - convert indentation to tabs
                        - side note:
                            - when highlighting the indentation:
                                - "Spaces" are indicated via dotes
                                - "Tabs" are indicated via an arrow
                - trim trailing whitespace
                    - continuing from the previous code example:
                        - add trailing whitespace after the print-statement --> trim it again
        - File Encoding:
            - click to reopen/save the active file with a different encoding --> drop-down list with available encodings
        - End of Line Sequence:
            - click to switch between [CRLF or LF][104]
        - Language Mode:
            - depicts the language of the active file --> click to switch to another language
                - example:
                    - open a Markdown file and then a Python file
            - if applicable, additional info is depicted --> e.g. for Python:
                - left to Language Mode: Python-specific notifications
                - right to Language Mode: current environment --> click to switch to or create* another environment
                    - *: there are two types of environments that you can create --> virtual and conda
        - [GitHub Copilot][172]
        - Notifications Bell:
            - a dot on the bell indicates that there are new notifications
                - example:
                    - create a file for a programming language that you haven't installed
                    - toolbar:
                        - more actions
                        - delete (individual notification)
            - click --> toolbar:
                - clear all notifications
                - toggle "Do Not Disturb"
                - hide notifications
    - side note:
        - additional information might be added to the status bar by different:
            - features within VS Code
                - e.g. [Source Control][19] --> currently checked out branch is depicted
            - extensions
                - e.g. [Jupyter][68] --> when a Jupyter Notebook file is opened, the number of the currently active cell and the total number of cells is depicted --> click to jump to the currently active cell
- # Misc
    - # Settings
        - VS Code is highly customizable* --> settings editor:
            - *:
                - nearly every part of VS Code's user interface or functional behavior can be modified
                - examples: check the references of [this reference link][12]
            - how to open:
                - [Command Palette][120]: "Preferences: Open Settings (UI)"
                - [Manage-icon][180] > Settings
                - [Menu Bar][71] > File > Preferences > Settings
            - lists all available settings ordered by category
                - left-hand side: tree-view for quick navigation
            - search bar:
                - filter the settings based on the entered search criteria --> right-hand side: number of search results
                    - search examples: minimap, font, local history
                - search actions:
                    - clear search input
                    - apply predefined filter(s):
                        - filter the settings based on specific meta-data about the settings* --> example filters:
                            - *:
                                - rather than filtering them based on text as with the regular search --> e.g. "@modified" vs "modified"
                            - modified:
                                - filter for all settings that differ from the default value --> [exception][190]
                            - feature:
                                - filter for a specific feature --> e.g. explorer
                            - tag:
                                - filter for a specific tag --> e.g. requireTrustedWorkspace
                            - language:
                                - filter for language-specific settings --> e.g. Python
                                - i.e. changes to such settings only apply to the [specific language][184]
                        - alternative:
                            - type the @-symbol directly into the search bar --> drop-down list with all available filters
                            - type to filter the list
                                - example: type "la" --> select "lang:" --> type "p" --> select "python"
                - side note:
                    - undo/redo is supported
                        - i.e. scroll through search history
            - structure of individual setting:
                - ID at the top
                    - i.e. the heading
                - short description
                - field to modify the setting
                    - e.g. a drop-down list with available options or an input field to directly input a value
                    - setting = modified --> indicated via blue bar on the left-hand side
                - gear icon* left to the ID:
                    - *:
                        - hover over the ID or click into the area of the setting to make it visible
                    - reset a setting to its default value
                    - copy:
                        - the setting ID
                        - the setting as a [JSON key-value pair][193]
                        - the setting URL
                            - enables you to directly navigate to a specific setting from the browser
                    - apply setting to all [profiles][8]
            - settings can be applied at different scopes:
                - user settings:
                    - apply globally
                        - i.e. apply to any instance of VS Code
                        - example:
                            - open a workspace and set the font size to 10 --> open:
                                - another workspace
                                - a new instance and create a new file
                - workspace settings:
                    - only apply to the respective workspace
                        - example:
                            - open a workspace and set the font size to 10 --> open another workspace
                    - side note:
                        - not all user settings are available as workspace settings
                            - e.g. application-wide settings related to updates or security can not be overridden by workspace settings
                                - example: search for "update" or "security" in the settings editor --> switch between user settings and workspace settings
                - workspace folder settings:
                    - only apply to the respective root folder within a [multi-root workspace][134]
                        - example:
                            - copy and open this [multi-root workspace][82]
                            - set the font size to 10 for "folder_1"
                            - open a file from "folder_1" and "folder_2"
                    - side notes:
                        - you can still set [workspace settings][182]:
                            - they apply to all root folders within the multi-root workspace
                                - continuing from the previous example:
                                    - reset the font size for "folder_1" to its default value
                                    - set the font size to 10 for the workspace
                        - to avoid setting collisions, only settings that affect the root folder or files within the root folder are applied --> not settings that affect the entire editor
                            - continuing from the previous example:
                                - the window.zoomLevel can not be specified separately for different root folders since it affects the entire editor
                - remote settings:
                    - only apply to the respective [remote][220]
                        - [example][186]
                - language-specific settings:
                    - only apply to the respective language
                        - stated in brackets
                        - example:
                            - select [Python][183] and set the font size to 10
                            - create a JavaScript file
                    - can be set for the user, workspace, workspace folder or remote scope
                    - side note:
                        - some languages have language-specific default settings
                            - example: open [defaultSettings.json][191] and search for "[python]"
                - side notes:
                    - [settings precedence][187]
                    - setting modified in a different scope --> indication* next to the setting ID:
                        - *:
                            - click to jump to the respective setting
                        - "modified in..."
                        - "modified elsewhere" --> hover to see a list
                            - example:
                                - set font size to 10 in the user settings --> switch to workspace settings
                                - set font size to 10 in language-specific user settings (e.g. for Python) --> switch back to workspace settings
            - [Backup and Sync Settings][229]-Button:
                - backup and sync your data across devices --> e.g. settings, [keyboard shortcuts][126], [snippets][4] etc.
                - alternative: [Accounts-icon][137] or [Manage-icon][180] --> "Backup and Sync Settings"
        - side notes:
            - the actual setting values are stored in a respective "settings.json" file*:
                - *:
                    - each [scope][194] has its own "settings.json" file --> exception: language-specific settings
                - how to open:
                    - Editor toolbar of settings editor
                    - [Command Palette][120]:
                        - "Preferences: Open User Settings (JSON)"
                        - "Preferences: Open Workspace Settings (JSON)"
                        - "Preferences: Open Folder Settings (JSON)"
                        - "Preferences: Open Default Settings (JSON)"
                    - manually:
                        - user settings --> file location:
                            - Windows: %APPDATA%\Roaming\Code\User\settings.json
                            - macOS: $HOME/Library/Application\ Support/Code/User/settings.json
                            - Linux: $HOME/.config/Code/User/settings.json
                        - workspace settings --> file location:
                            - ".vscode" folder in the root of the workspace --> gets created when workspace settings are modified
                        - workspace folder settings --> file locations:
                            - workspace folder settings: ".vscode" folder in the respective root folder --> gets created when respective workspace folder settings are modified
                                - example: copy and open [this][82] multi-root workspace
                            - workspace settings: [".code-workspace" file][188]
                - settings can also be directly edited within the respective "settings.json" file*:
                    - *:
                        - the settings editor is simply a graphical interface to manage the settings
                    - settings are written as JSON by specifying the setting ID and a value --> full [IntelliSense][155] available*
                        - *:
                            - i.e. member lists for settings IDs and values + quick info
                        - code examples:
                            - general settings:
                                - ```json
                                    {
                                        "editor.fontSize": 16,
                                        "files.autoSave": "afterDelay",
                                    }
                                    ```
                            - language-specific settings:
                                - ```json
                                    {
                                        "[python]": {
                                            "editor.fontSize": 18,
                                            "files.autoSave": "off",
                                        }
                                    }
                                    ```
                    - side notes:
                        - hover left to line number --> button to edit the setting*
                            - *:
                                - only available for settings with predefined options
                            - continuing from the previous code example:
                                - the button is available for "files.autoSave" but not for "editor.fontSize"
                        - if a setting is explicitly set within a "settings.json" file, then it is listed as "modified" in the settings editor*
                            - *:
                                - even if it is set to the default value
                            - continuing from the previous code example:
                                - set the "editor.fontSize" to 14 
                        - to reset a setting to its default value:
                            - comment out the setting
                            - delete the setting
                        - some settings can only be edited in "settings.json" files:
                            - e.g. workbench.colorCustomizations --> "Edit in settings.json"-link
                        - the "workbench.settings.editor"-setting:
                            - determines if the settings editor or the "settings.json" files are used as the default
                            - i.e. the settings editor or the "settings.json" files respectively are opened when using:
                                - keyboard shortcut: Ctrl+,
                                - [Manage-icon][180] > Settings
                                - [Menu Bar][71] > File > Preferences > Settings 
            - VS Code's features and their corresponding settings can be in one of the following states:
                - experimental:
                    - exploratory features available for early adopters --> might change or be removed in the future
                    - they have an "Experimental"-label in the settings editor --> searchable via [@tag:experimental][189]
                - preview:
                    - features have the final functionality but might still be iterated on for stability and polishing
                    - they have a "Preview"-label in the settings editor --> searchable via [@tag:preview][189]
                - stable:
                    - features are stable and fully supported in VS Code
            - settings and security:
                - some settings allow you to specify an executable that VS Code will run to perform certain operations --> for enhanced security, such settings can only be defined in user settings and not in workspace settings
                - examples:
                    - git.path
                    - terminal.external.windowsExec
                    - terminal.external.osxExec
                    - terminal.external.linuxExec
    - # UI Customization
        - hiding or repositioning different UI elements:
            - [Layout Controls][67] --> Customize Layout-button:
                - hide/toggle the [Menu Bar][71], [Activity Bar][65], Primary/Secondary Side Bar, [Panel][10], [Status Bar][9]
                - adjust Primary Side Bar position
                - adjust the [Panel][10] alignment
                    - side note:
                        - Panel toolbar: "maximize"-button only available for alignment option "center"
                - adjust the Quick Input* position
                    - *:
                        - i.e. the [Command Center][6]
                    - side note:
                        - move the Quick Input anywhere you like by grabbing the top edge with the mouse cursor --> window snaps to the center (horizontally or vertically) or to the top
                - toggle [Full Screen, Zen Mode or Centered Layout][125]
            - [Menu Bar][71] > View > Appearance:
                - Activity Bar Position
                    - when selecting the top or bottom position, the [Accounts-icon][137] and [Mange-icon][180] move to the right side of the [Title Bar][197]
                - Panel Position
                - Editor Actions Position
                - Zoom in/out --> reset
            - context menu:
                - right-click the element or the respective area that it belongs to --> examples:
                    - parts of the [Title Bar][197]
                    - icons in the [Activity Bar][65]
                    - views in the [Activity Bar][65] --> right-click the top
                    - views in the [Panel][10] --> right-click the top
                    - elements in the [Status Bar][9]
                    - toolbar actions*:
                        - *:
                            - they get moved to the overflow menu --> right-click the overflow menu to toggle it on again
                        - toolbar of the Folders-view in the [Explorer][14]
                        - toolbar of the [Search-view][64]
                        - toolbar of the [Editor][13]
                        - side note:
                            - [Command Palette][120]: "View: Reset All Menus"
        - changing themes:
            - color theme:
                - affects UI elements and syntax highlighting
                - open the color theme picker via:
                    - [Command Palette][120]: "Preferences: Color Theme"
                    - [Manage-icon][180] > Themes > Color Theme
                    - [Menu Bar][71] > File > Preferences > Themes > Color Theme
                - additional themes can be installed via [Extensions][7]
                    - e.g. github.github-vscode-theme
                - side note:
                    - themes can be further [customized][231]
            - file icon theme:
                - affects the file icons in the [Explorer][14] and in [tabs][196]
                - open the file icon theme picker via:
                    - [Command Palette][120]: "Preferences: File Icon Theme"
                    - [Manage-icon][180] > Themes > File Icon Theme
                    - [Menu Bar][71] > File > Preferences > Themes > File Icon Theme
                - additional themes can be installed via [Extensions][7]
                    - e.g. pkief.material-icon-theme
            - product icon theme:
                - affects all* the built-in icons in VS Code
                    - *:
                        - except file icons and icons contributed by extensions
                    - e.g.:
                        - icons in the [Activity Bar][65]
                        - icons in search bars or toolbars
                        - icons in the [Extensions][7] side bar
                        - icons in the [Layout Controls][67]
                        - folding arrows in the [Editor][13] or [Explorer][14]
                        - breakpoints
                - open the product icon theme picker via:
                    - [Command Palette][120]: "Preferences: Product Icon Theme"
                    - [Manage-icon][180] > Themes > Product Icon Theme
                    - [Menu Bar][71] > File > Preferences > Themes > Product Icon Theme
                - additional themes must be installed via [Extensions][7]
                    - e.g. pkief.material-product-icons
        - rearranging views:
            - they can be:
                - reordered
                    - examples:
                        - reorder the activity icons in the [Activity Bar][65]
                        - reorder the views in the [Explorer][14]
                        - reorder the views in the [Panel][10]
                - moved into different locations
                    - examples:
                        - move the [Explorer][14] into the [Panel][10] --> as an additional view or within an already existing view
                        - move the [Outline-view][166] into the [Panel][10] --> as an additional view or within an already existing view
                        - move the [Problems-view][157] into the [Activity Bar][65] --> as an additional view or within an already existing view
                        - move the [Outline-view][166] into the secondary side bar
            - resetting them to the default location:
                - right-click the respective activity or view --> "Reset Location"
                - [Command Palette][120]: "View: Reset View Locations"
        - resizing windows:
            - if available, sashes are highlighted in blue* when hovering
                - *:
                    - for the default color theme
                - examples:
                    - on the right/left of the primary/secondary side bar
                    - at the top of views in the primary side bar --> e.g. [Explorer][14]
                    - at the top of the [Panel][10]
                    - between [multiple editor groups][204]
                    - on the left of the ["search within file"-functionality][123]
                    - at the left/right and bottom of the [quick info][205]
            - drag the sash to resize the window
            - double-click the sash to reset the window to its default size
        - side notes:
            - changing the display language:
                - [Command Palette][120]: "Configure Display Language"
            - [Settings][12]:
                - a lot of the UI elements or functional behavior can be customized via the settings --> check the references of [this reference link][12] to see all the mentioned settings throughout these notes
    - # Keyboard Shortcuts
        - example shortcuts*:
            - *:
                - [shortcuts reference][211]:
                    - assumes a US English keyboard --> VS Code automatically adjusts some of the shortcuts based on the current system's keyboard layout
                        - [example shortcut][219]
                    - is also available via [Menu Bar][71]: Help > Keyboard Shortcut Reference
                - shortcuts are also listed throughout the entire UI:
                    - e.g. [Command Palette][120], [Menu Bar][71], context menu, when hovering on buttons etc.
                    - i.e. if you use a certain functionality regularly, then you can easily learn the respective shortcut
            - the single most important command:
                - accessing the [Command Palette][120]:     Ctrl+Shift+P
                    - technically this is the only shortcut you need --> you can access all of VS Code's functionality + learn the respective keyboard shortcut (if available)
            - accessing UI elements:
                - [Title Bar][197]:
                    - [Menu Bar][71]:                       Alt
                        - use arrow keys for navigation
                        - press Alt again to return to previous focus
                    - [Layout Controls][67]:
                        - toggle primary side bar:          Ctrl+B
                        - toggle secondary side bar:        Ctrl+Alt+B
                        - toggle panel:                     Ctrl+J
                - [Activity Bar][65]:
                    - [Explorer][14]:                       Ctrl+Shift+E
                        - use arrow keys for navigation
                            - UpArrow/DownArrow: move up down
                            - LeftArrow/RightArrow: toggle folders* --> if focus is on file/folder within a folder, then focus jumps to folder
                                - *: alternatively: Enter
                        - press first letter(s) of the respective file/folder to focus it
                    - [Search][64]:                         Ctrl+Shift+F
                        - Replace:                              Ctrl+Shift+H
                        - toggle search details:                Ctrl+Shift+J
                        - focus next/previous search result:    F4 / Shift+F4
                    - [Source Control][19]:                 Ctrl+Shift+G
                    - [Debugger][30]:                       Ctrl+Shift+D
                    - [Extensions][7]:                      Ctrl+Shift+X
                    - side note:
                        - press respective shortcut again to return focus to Editor --> exception: Search
                - [Editor][13]:
                    - focus 1st/2nd/...:
                        - editor group:                     Ctrl+1/2/...
                            - if number doesn't exist, then a new empty editor group is created
                            - Ctrl+0 --> focuses side bar
                        - editor in active editor group:    Alt+1/2/...
                            - cycle through editors:            Ctrl+Tab
                                - lists most recently opened editors first --> i.e. you can easily switch back and forth between two editors
                - [Panel][10]:
                    - [Problems-view][157]:                 Ctrl+Shift+M
                    - [Output-View][143]:                   Ctrl+Shift+U
                    - [Debug Console][153]:                 Ctrl+Shift+Y
                    - [Terminal][160]:                      Ctrl+Ö
                        - US:                                   Ctrl+"backtick"
                - Misc:
                    - [Settings][12]:                       Ctrl+, 
                    - [Keyboard Shortcuts Editor][53]:      Ctrl+K Ctrl+S
                - side notes:
                    - switch between input control/result:  Ctrl+UpArrow/DownArrow
                        - e.g. [Extensions-view][7], [Keyboard Shortcuts Editor][53], [Settings Editor][232], [Problems-view][157] or [Debug Console][153]
                    - toggle Tab-navigation:                Ctrl+M
                        - activation is indicated via [Status Bar][9]
                        - enables you to cycle through all the UI components via Tab or Shift+Tab --> orientation: left to right and/or top to bottom
                        - i.e. this way you can access all the UI components that don't have a default shortcut --> e.g. [Command Center][6], [Customize Layout-button][212], [Ports-view][171], [Status Bar][9], [Accounts-icon][137] or [Mange-icon][180]
                        - use arrow keys to access the different elements within an UI component --> e.g. icons of the activity bar, elements in the status bar, actions in toolbars, etc.
                    - focus next/previous element:          F6 / Shift+F6
                        - cycles focus between editor, panel, status bar, activity bar and primary sidebar
            - file/editor management:
                - open:
                    - [file][213]:                  Ctrl+P
                        - alternatively via:
                            - File Explorer:            Ctrl+O
                            - [Explorer][218]
                    - folder/workspace:             Ctrl+K Ctrl+O
                    - recent:                       Ctrl+R
                        - especially useful for quickly switching between workspaces
                - create new:
                    - file/editor:                  Ctrl+N
                    - window:                       Ctrl+Shift+N
                - save:
                    - file:                         Ctrl+S
                    - file as:                      Ctrl+Shift+S
                    - all:                          Ctrl+K S
                - close:
                    - file/editor:                  Ctrl+W
                        - reopen closed editor:         Ctrl+Shift+T
                    - window:                       Ctrl+Shift+W
                    - all editors in group:         Ctrl+K W
                    - all editors:                  Ctrl+K Ctrl+W
                    - folder/workspace:             Ctrl+K F
                - split editor:
                    - right:                        Ctrl+^
                        - US:                           Ctrl+\
                    - up:                           Ctrl+K Ctrl+^
                        - US:                           Ctrl+K Ctrl+\
                - move:
                    - editor tab left/right:        Ctrl+Shift+PageUp/PageDown
                    - editor into another group:    Ctrl+Alt+Left-/RightArrow
                    - active editor group:          Ctrl+K Left-/Right-/Down-/UpArrow
            - [Editor][13]:
                - basic editing:
                    - cut/copy/paste:               Ctrl+X/C/V
                        - code example:
                            - ```python
                                n_1 = 1
                                n_3 = 3
                                n_2 = 2
                                
                                numbers = []
                                for i in range(5):
                                    numbers.append(i)
                                
                                print(numbers)
                                ```
                            - empty selection --> cut/copy/paste line
                    - undo/redo:                    Ctrl+Z / Ctrl+Shift+Z
                    - move line up/down:            Alt+UpArrow/DownArrow
                    - copy line up/down:            Shift+Alt+UpArrow/DownArrow
                    - insert line below or above:   Ctrl+Enter / Ctrl+Shift+Enter
                    - indent or outdent line:       Tab or Shift+Tab
                    - fold/unfold:
                        - region:                   Ctrl+Shift+ß/´
                            - US:                       Ctrl+Shift+[/]
                        - all subregions:           Ctrl+K Ctrl+ß/´
                            - US:                       Ctrl+K Ctrl+[/]
                        - all:                      Ctrl+K Ctrl+0/J
                        - 1st/2nd/.../7th level:    Ctrl+K Ctrl+1/2/.../7
                            - code example:
                                - ```markdown
                                    - level 1
                                        - level 2
                                            - level 3
                                                - level 4
                                                    - level 5
                                                        - level 6
                                                            - level 7
                                                                - level 8
                                                                    - level 9
                                    - level 1
                                        - level 2
                                            - level 3
                                                - level 4
                                                    - level 5
                                                        - level 6
                                                            - level 7
                                                                - level 8
                                                                    - level 9
                                    - level 1
                                        - level 2
                                            - level 3
                                                - level 4
                                                    - level 5
                                                        - level 6
                                                            - level 7
                                                                - level 8
                                                                    - level 9
                                    ```
                                - fold to level 8 --> doesn't work
                                - fold to level 7
                                - fold to level 3
                            - only works for folding and not unfolding
                            - exception: when cursor is in the folded region
                                - continuing from the previous code example:
                                    - put cursor on first "level 3"
                                    - fold to level 5
                                    - fold to level 1
                        - [marker regions][234]     Ctrl+K Ctrl+8/9
                            - continuing from the previous code example:
                                - add "<!-- #region -->" before and "<!-- #endregion -->" after first nested list
                    - [Intellisense][155]:
                        - member lists:             Ctrl+Space
                            - code example:
                                - ```python
                                    number = 1 
                                    pr
                                    ```
                        - quick info:               Ctrl+Space again
                        - parameter hints:          Ctrl+Shift+Space
                            - code example:
                                - ```python
                                    number = 1 
                                    print()
                                    ```
                        - show hover:               Ctrl+K Ctrl+I
                            - code example:
                                - ```python
                                    number = 1 
                                    print(number)
                                    ```
                                - put the cursor on "print" and show hover
                                - put the cursor on "numbers" and show hover
                    - [Code Actions][169]:          Ctrl+.
                        - [code example][216]
                    - [format][209]:
                        - document:                 Shift+Alt+F
                        - selection:                Ctrl+K Ctrl+F
                            - [code example][217]
                    - toggle:
                        - line comment:             Ctrl+#
                            - US:                       Ctrl+/
                        - block comment:            Shift+Alt+A
                    - side notes:
                        - rename symbol:            F2
                            - continuing from the cut/copy/paste-example:
                                - rename "numbers" to "list_of_numbers"
                        - toggle breakpoint:        F9
                        - show editor context menu: Shift+F10
                - code navigation:
                    - move cursor:
                        - to beginning/end of line:         Home/End
                        - to beginning/end of file:         Ctrl+Home/End
                        - one word to the left/right:       Ctrl+Left/RightArrow
                        - back/forward:                     Alt+Left/RightArrow
                        - to matching bracket:              Ctrl+Shift+^
                            - US:                               Ctrl+Shift+\
                            - code example:
                                - ```python
                                    data_base = [
                                        {"id": 1, "user": "John"},
                                        {"id": 2, "user": "Jane"},
                                        {"id": 3, "user": "Bill"}
                                    ]
                                    ```
                        - side note:
                            - to next/previous symbol highlight: F7 / Shift+F7
                    - scroll:
                        - line up/down:                     Ctrl+Up/DownArrow 
                        - page up/down:                     Alt+PgUp/PgDn 
                    - [Command Center][6]-functionality:
                        - go to line:                       Ctrl+G
                        - go to symbol in file:             Ctrl+Shift+O
                        - go to symbol in workspace:        Ctrl+T
                    - [search][123]:                        Ctrl+F
                        - replace:                              Ctrl+H
                    - [breadcrumbs][210]:                   Ctrl+Shift+.
                        - [code example][29]
                        - use arrow keys to navigate
                    - zoom in/out:                          Ctrl+ +/-
                        - US:                                   Ctrl+ =/-
                - selections/multiple cursors:
                    - select current line:                          Ctrl+L
                    - select all occurrences:                       Ctrl+Shift+L
                    - add next occurrence to selection:             Ctrl+D
                        - if selection empty, then the word, that the cursor is on, is selected
                        - move last selection to next occurrence:       Ctrl+K Ctrl+D
                            - continuing from the cut/copy/paste-example:
                                - select the first and third occurrences of "list_of_numbers"
                    - undo last cursor operation:                   Ctrl+U
                    - shrink/expand selection:                      Shift+Alt+Left/RightArrow
                    - insert cursor at end of each line selected:   Shift+Alt+I
                        - continuing from the cut/copy/paste-example:
                            - add two zeros to each value of "n_1", "n_2" and "n_3"
                    - insert cursor above/below:                    Ctrl+Alt+Up/DownArrow
                        - continuing from the cut/copy/paste-example:
                            - transform "n" to "number" for "n_1", "n_2" and "n_3"
            - [integrated Terminal][160]:
                - scroll to previous/next command:          Ctrl+UpArrow/DownArrow
                - scroll to top/bottom:                     Ctrl+Home/End
                - scroll page up/down:                      Ctrl+Shift+PageUp/PageDown
                - scroll line up/down:                      Ctrl+Alt+PageUp/PageDown
                - create new terminal:                      Ctrl+Shift+Ö
                    - US:                                      Ctrl+Shift+"backtick"
                - split terminal:                           Ctrl+Shift+5
                - focus next terminal group:                Ctrl+PageDown
                - focus next terminal in terminal group:    Alt+DownArrow
                - go to recent directory:                   Ctrl+G
                - open detected links:                      Ctrl+Shift+O
                    - opens a searchable Quick Pick with all detected links (including word links)
                    - [code example][43]
            - side notes:
                - exit whatever you have triggered:         Esc
                    - e.g. parameter hints, search, context menu, command palette etc.
                - other key mappings can be installed via [Extensions][7]
                    - examples: click ["Filter Extensions"][135] > Category > Keymaps
        - Keyboard Shortcuts Editor:
            - how to open:
                - [Command Palette][120]: "Preferences: Open Keyboard Shortcuts"
                - [Manage-icon][180] > Keyboard Shortcuts
                - [Menu Bar][71]: File > Preferences > Keyboard Shortcuts
            - lists all available commands with and without keyboard shortcuts --> structure:
                - command name
                - keybinding (if available)
                - when-clause --> i.e. condition(s) when the keybinding applies
                - source --> e.g. System*, respective Extension or User
                    - *: i.e. default commands
            - filter the list via the search box:
                - search examples:
                    - format
                    - undo
                    - insert cursor
                - search options:
                    - record keys
                        - examples:
                            - Ctrl+F
                            - Ctrl+Shift+F
                            - Ctrl+K Ctrl+F
                    - sort by precedence*
                        - *:
                            - highest precedence at the bottom
                        - example:
                            - Ctrl+B:
                                - toggle side bar --> source: System
                                - toggle bold     --> source: [Markdown All in One][48]-extension
                                - create your own keybinding --> source: User
                    - clear input
            - modify/manage the keybindings via the context menu:
                - Copy:
                    - (JSON object)
                    - Command ID
                    - Command Title
                - Change Keybinding
                    - after inputting a keybinding: indication of how many other commands have the same keybinding
                    - example: change any command to have the keybinding "Ctrl+F" vs "Ctrl+Shift+Alt+F"
                - Add Keybinding
                    - example: add the keybinding "alt+b" for the command "Toggle Primary Side Bar Visibility"
                - Remove Keybinding
                - Reset Keybinding
                - Change When Expression
                    - [Intellisense][155] is available
                    - [conditional operators][215]
                - Show Same Keybindings
                    - example: Accept Inline Completion --> Ctrl+#
            - editor toolbar:
                - Open Keyboard Shortcuts (JSON)*:
                    - *:
                        - alternatively via [Command Palette][120]:
                            - "Open Keyboard Shortcuts (JSON)"
                            - "Open Default Keyboard Shortcuts (JSON)"
                    - any changes made to the keybindings are stored in this file
                        - example:
                            - change the keybinding of the command "Toggle Primary Side Bar Visibility" to "alt+b" via the Keyboard Shortcuts Editor
                        - side note:
                            - a "-" in front of the command name indicates a removal rule
                    - you can also directly modify the keybindings in the "keybindings.json"-file
                        - add a new entry via [Intellisense][155] or via the blue "Define Keybinding"-button
                        - example:
                            - ```json
                                {
                                    "key": "alt+s",
                                    "command": "saveAll",
                                }
                                ```
                    - side notes:
                        - disable a keyboard shortcut by specifying an empty action
                            - example:
                                - ```json
                                    {
                                        "key": "ctrl+f",
                                        "command": "",
                                    }
                                    ```
                            - this way "ctrl+f" doesn't work in any of the when-conditions --> e.g. when editor or terminal is focused
                        - advanced customizations:
                            - [command arguments][100]
                            - [running multiple commands][109]
                - overflow menu:
                    - Show Extension/System/User Keybindings
            - side notes:
                - customizing a keyboard shortcut for a UI action:
                    - right-click on any action item and select "Configure Keybinding" --> opens Keyboard Shortcuts editor filtered to the corresponding command (including the respective when-clause)
                        - example: "Collapse Folders"-button in [Explorer][14] toolbar
                            - specify the shortcut to be "Ctrl+Shift+Alt+C"
                            - the when clause "view == 'workbench.explorer.fileView'" means that the Folders-view must be focused --> i.e. the section header
                            - to make the shortcut work in all circumstances delete the when-clause
                - troubleshooting keyboard shortcut conflicts:
                    - [Command Palette][120]: "Developer: Toggle Keyboard Shortcuts Troubleshooting"
                    - activates logging of dispatched keyboard shortcuts and opens the [Output-view][143]
- #
- code editor:
    - free
    - cross-platform --> Windows, Linux, macOS
    - maintained by Microsoft --> [monthly updates][1] with new features and bug fixes
- side notes:
    - [official documentation][2]:
        - main resource for these notes
        - tree-navigation on the left-hand side --> structure (imo):
            - part 1 --> setup & getting started
                - "get started" provides high-level information to quickly get up and running
            - part 2 --> how to use the editor
                - configure
                - edit code
                - build, debug, test
                - source control
                - terminal
                - GitHub Copilot
            - part 3 --> language-specific information
                - general overview and short introduction to different languages
                - more detailed information for some selected languages --> e.g. JavaScript, Python, C++ etc.
            - part 4 --> miscellaneous topics
                - container tools
                - data science
                - intelligent apps
                - Azure
                - remote
                - dev containers
                - reference
        - input field to search across the documentation in the top-right corner
    - checking the current version:
        - [Menu Bar][71]: Help > About
    - "insiders edition":
        - daily updates --> may lead to the occasional broken build
        - can be installed side-by-side with the monthly stable build
    - "Welcome Page":
        - by default, a "Welcome Page" is shown at startup* --> toggle off the check box at the bottom to disable it
            - *: if no editors are restored from the previous session
        - alternatively via [Settings][12]: workbench.startupEditor
    - [VS Code][113] versus [Code OSS][114] versus [VSCodium][115]:
        - VS Code is "built on open source":
            - the code for the actual editor ("Code OSS") is released under the [MIT License][105] --> this is open source
            - however, VS Code is actually released under the [Microsoft Software License][106] --> i.e. this is not open source
        - Microsoft takes Code OSS and adds [specific customizations][107] to create VS Code --> e.g.:
            - Microsoft trademarks (e.g. logos and product names)
            - integration of the [Visual Studio Marketplace][99]
            - telemetry:
                - can be turned off --> [Settings][12]: telemetry.telemetryLevel
                - note: [extensions][7] may be collecting their own usage data and are not controlled by this setting --> consult the specific extension's documentation to learn about its telemetry reporting and whether it can be disabled
        - if you want the open source version, then:
            - build Code OSS [from source][112]
            - use VSCodium
                - they have already built Code OSS from source
    - additional topics*:
        - *:
            - i.e. topics that are not covered in detail in these notes
        - [command-line interface][221]
            - enables you to control how VS Code is launched
        - [GitHub Copilot][222]
            - enables you to use the GitHub Copilot AI features directly within VS Code
        - [profiles][223]
            - useful because VS Code can be highly personalized via [Extensions][7], [Settings][12] or [UI Customizations][227]
            - profiles enable you to create sets of customizations --> quickly switch between them and/or share them with others
        - [remote development][224]
            - enables you to develop your project locally while the actual codes is stored and executed on a remote server
        - [snippets][225]
            - enable you to quickly enter repeating code patterns instead of manually typing them
        - [tasks][226]
            - useful because there are lots of tools for automating specific processes --> e.g. the TypeScript Compiler, ESLint, Gulp, Rake etc.
            - tasks enable you to run these tools* directly from within VS Code
                - *: or any other automated command-line processes
- 
























[197]: #title-bar
[71]:  #title-bar "Title Bar > elements > Menu Bar"
[147]: #title-bar "Title Bar > elements > Menu Bar > provides access to... > Run"
[6]:   #title-bar "Title Bar > elements > Command Center"
[213]: #title-bar "Title Bar > elements > Command Center > click into search... > first section... > Go to File"
[120]: #title-bar "Title Bar > elements > Command Center > click into search... > first section... > Show and Run Commands"
[66]:  #title-bar "Title Bar > elements > Command Center > click into search... > first section... > More > select the command... > :"
[67]:  #title-bar "Title Bar > elements > Layout Controls"
[212]: #title-bar "Title Bar > elements > Layout Controls > Customize Layout button"
[199]: #title-bar "Title Bar > elements > Layout Controls > buttons to toggle... > Panel"

[65]:  #activity-bar
[137]: #activity-bar "Activity Bar > side notes > Accounts-icon"
[180]: #activity-bar "Activity Bar > side notes > Manage-icon"
[214]: #activity-bar "Activity Bar > side notes > icons can display... > examples > Source Control..."
[179]: #activity-bar "Activity Bar > side notes > icons can display... > examples > Debugger..."
[132]: #activity-bar "Activity Bar > side notes > search within views"

[14]:  #explorer
[122]: #explorer "Explorer > workspace"
[136]: #explorer "Explorer > workspace > open/close workspace"
[134]: #explorer "Explorer > workspace > accessing files/folders... > or create a..."
[188]: #explorer "Explorer > workspace > accessing files/folders... > or create a... > Menu Bar... > Close Workspace > continuing from the... > close the workspace... > *"
[230]: #explorer "Explorer > workspace > workspace trust > when using VS Code..."
[202]: #explorer "Explorer > workspace > workspace trust > when using VS Code... > toy-example"
[124]: #explorer "Explorer > purpose > to browse and... > manage > clicking > single-click..."
[192]: #explorer "Explorer > the different views > open editors-view"
[130]: #explorer "Explorer > the different views > open editors-view > toolbar > close all editors..."
[166]: #explorer "Explorer > the different views > outline-view"
[11]:  #explorer "Explorer > side notes > hidden files/folders"
[18]:  #explorer "Explorer > side notes > hidden files/folders > specify which files/folders..."

[64]: #search

[19]:  #source-control
[181]: #source-control "Source Control > inspecting the commit... > (mainly) via Graph-view > click a commit..."
[139]: #source-control "Source Control > inspecting the commit... > (mainly) via Graph-view > toolbar"
[138]: #source-control "Source Control > inspecting the commit... > (alternatively) via Timeline-view..."
[133]: #source-control "Source Control > inspecting the commit... > (alternatively) via Timeline-view... > click a commit..."
[240]: #source-control "Source Control > inspecting the commit... > (alternatively) via Timeline-view... > click a commit... > toolbar > map-icon... > side notes > available adjustments via... > diffEditor.hideUnchangedRegions.revealLineCount"
[176]: #source-control "Source Control > creating commits > manage the changes... > Changes-section > open changes > i.e. open diff(s)... > overflow menu..."
[237]: #source-control "Source Control > creating commits > side notes > click a file... > there are gutter..."

[30]:  #debugger
[149]: #debugger "Debugger > terminology > debugger"
[173]: #debugger "Debugger > basic functionality > setting breakpoints > Breakpoints-view"
[207]: #debugger "Debugger > basic functionality > running the debugger"
[175]: #debugger "Debugger > basic functionality > running the debugger > side notes > alternatively the debugger..."
[198]: #debugger "Debugger > basic functionality > inspect its state... > Variables"
[17]:  #debugger "Debugger > basic functionality > inspect its state... > Watch"
[153]: #debugger "Debugger > basic functionality > using the debug console"
[174]: #debugger "Debugger > basic functionality > side notes > multiple debugger sessions"
[150]: #debugger "Debugger > basic functionality > side notes > Just My Code-setting"
[144]: #debugger "Debugger > advanced functionality > different types of..."
[151]: #debugger "Debugger > advanced functionality > different types of... > logpoints"
[152]: #debugger "Debugger > advanced functionality > different types of... > logpoints > usage > side note"
[145]: #debugger "Debugger > advanced functionality > different types of... > function breakpoints"
[154]: #debugger "Debugger > advanced functionality > different types of... > exception breakpoints > side note"
[146]: #debugger "Debugger > advanced functionality > launch configurations"
[27]:  #debugger "Debugger > advanced functionality > launch configurations > two types > automatic"
[140]: #debugger "Debugger > advanced functionality > launch configurations > two types > manual/customized"

[7]:   #extensions
[135]: #extensions "searching extensions > side notes > search options > filter"
[236]: #extensions "side notes > measures undertaken by..."

[162]: #jupyter "Jupyter > Jupyter Notebook > notebook toolbar > third section > Jupyter Variables"
[77]:  #jupyter "Jupyter > Jupyter Notebook > code cells > cell status bar > language picker"
[72]:  #jupyter "Jupyter > Jupyter Notebook > side notes > interaction with cells > collapse/expand cell..."
[167]: #jupyter "Jupyter > Jupyter Notebook > side notes > working with plots"
[161]: #jupyter "Jupyter > Python Interactive Window > side notes > Jupyter-like cells..."
[163]: #jupyter "Jupyter > extension pack > Jupyter Keymap"
[165]: #jupyter "Jupyter > extension pack > Jupyter Cell Tags"
[164]: #jupyter "Jupyter > extension pack > Jupyter Slide Show"

[13]:  #editor
[125]: #editor "Editor > modifying the editor..."
[204]: #editor "Editor > modifying the editor... > multiple editor groups"
[155]: #editor "Editor > code editing > IntelliSense"
[205]: #editor "Editor > code editing > IntelliSense > quick info..."
[169]: #editor "Editor > code editing > Code Actions > click lightbulb to... > quick fixes"
[216]: #editor "Editor > code editing > Code Actions > click lightbulb to... > quick fixes > code examples"
[209]: #editor "Editor > code editing > code formatting"
[217]: #editor "Editor > code editing > code formatting > format actions > Format Selection > code example"
[168]: #editor "Editor > code editing > side notes > linting"
[28]:  #editor "Editor > code editing > side notes > multiple cursors/selections"
[121]: #editor "Editor > code navigation"
[196]: #editor "Editor > code navigation > tabs"
[127]: #editor "Editor > code navigation > tabs > actions > right-click > Pin"
[129]: #editor "Editor > code navigation > tabs > other related Settings > workbench.editor.showTabs"
[210]: #editor "Editor > code navigation > breadcrumbs"
[158]: #editor "Editor > code navigation > scrolling > overview ruler"
[159]: #editor "Editor > code navigation > scrolling > minimap"
[123]: #editor "Editor > code navigation > search within file"
[177]: #editor "Editor > code navigation > go to-functionality... > go to definition > if there are... > *"
[234]: #editor "Editor > code navigation > side notes > folding > side note > regions can also..."
[73]:  #editor "Editor > running code > language-specific functionality... > play-button in..."
[148]: #editor "Editor > running code > language-specific functionality... > play-button in... > drop-down arrow..."
[51]:  #editor "Editor > running code > language-specific functionality... > the Python REPL..."
[16]:  #editor "Editor > running code > language-specific functionality... > running just a..."
[178]: #editor "Editor > side notes > Editor toolbar... > Close All"
[116]: #editor "Editor > side notes > Editor toolbar... > Enable Preview Editors"

[10]:  #panel
[157]: #panel "Panel > default views > Problems"
[143]: #panel "Panel > default views > Output"
[160]: #panel "Panel > default views > Terminal"
[111]: #panel "Panel > default views > Terminal > toolbar > name of current... > click to open... > move terminal into..."
[43]:  #panel "Panel > default views > Terminal > side notes > all text in... > code example"
[171]: #panel "Panel > default views > Ports"

[9]:   #status-bar
[156]: #status-bar "Status Bar > provides information... > Errors/Warnings/Infos"

[12]:  #settings
[232]: #settings "Settings > VS Code is..."
[189]: #settings "Settings > VS Code is... > search bar > search actions > apply predefined filter(s) > filter the settings... > tag"
[183]: #settings "Settings > VS Code is... > search bar > search actions > apply predefined filter(s) > filter the settings... > language"
[194]: #settings "Settings > VS Code is... > settings can be..."
[184]: #settings "Settings > VS Code is... > settings can be... > language-specific settings"
[128]: #settings "Settings > side notes > the actual setting..."
[191]: #settings "Settings > side notes > the actual setting... > how to open > Command Palette > Preferences: Open Default..."
[193]: #settings "Settings > side notes > the actual setting... > settings can also... > settings are written..."
[190]: #settings "Settings > side notes > the actual setting... > settings can also... > side notes > if a setting... > *"

[227]: #ui-customization
[203]: #ui-customization "UI Customization > hiding or repositioning... > Layout Controls..."
[24]:  #ui-customization "UI Customization > changing themes"
[170]: #ui-customization "UI Customization > changing themes > color theme"
[206]: #ui-customization "UI Customization > resizing windows"

[126]: #keyboard-shortcuts
[218]: #keyboard-shortcuts "Keyboard Shortcuts > example shortcuts > accessing UI elements > Activity Bar > Explorer"
[200]: #keyboard-shortcuts "Keyboard Shortcuts > example shortcuts > file/editor management > open > recent"
[208]: #keyboard-shortcuts "Keyboard Shortcuts > example shortcuts > Editor > basic editing > IntelliSense"
[235]: #keyboard-shortcuts "Keyboard Shortcuts > example shortcuts > Editor > basic editing > Code Actions"
[219]: #keyboard-shortcuts "Keyboard Shortcuts > example shortcuts > Editor > basic editing > toggle > line comment"
[53]:  #keyboard-shortcuts "Keyboard Shortcuts > Keyboard Shortcuts Editor"

[172]: #-2 "side notes > additional topics > GitHub Copilot"
[8]:   #-2 "side notes > additional topics > profiles"
[220]: #-2 "side notes > additional topics > remote development"
[4]:   #-2 "side notes > additional topics > snippets"
[5]:   #-2 "side notes > additional topics > tasks"



[119]: demonstration_examples/debugger/
[91]:  demonstration_examples/debugger/basic_functionality.py
[93]:  demonstration_examples/debugger/my_library_code.py
[92]:  demonstration_examples/debugger/my_module.py
[29]:  demonstration_examples/editor/code_navigation.py
[201]: demonstration_examples/editor/sticky_scroll.md
[82]:  demonstration_examples/explorer/multi_root_workspace/
[74]:  demonstration_examples/explorer/workspace_trust
[80]:  demonstration_examples/explorer/outline_view.md
[79]:  demonstration_examples/explorer/outline_view.py
[61]:  demonstration_examples/jupyter/markdown_headings.ipynb
[62]:  demonstration_examples/jupyter/notebook_1.ipynb
[63]:  demonstration_examples/jupyter/notebook_2.ipynb
[58]:  demonstration_examples/jupyter/slide_show_after.ipynb
[102]: demonstration_examples/jupyter/slide_show_before.ipynb
[103]: demonstration_examples/jupyter/slide_show.slides.html
[86]:  demonstration_examples/source_control/
[83]:  demonstration_examples/source_control/diff_editor/
[20]:  demonstration_examples/source_control/diff_editor/diff_editor.py
[22]:  demonstration_examples/source_control/diff_editor/file_1.py
[23]:  demonstration_examples/source_control/diff_editor/file_2.py
[117]: demonstration_examples/source_control/graph_view/
[110]: demonstration_examples/source_control/initial_folder
[87]:  demonstration_examples/source_control/initial_repo/



[1]: https://code.visualstudio.com/updates
[2]: https://code.visualstudio.com/docs
[3]: https://code.visualstudio.com/docs/editor/intellisense#_types-of-completions
[15]: https://jupyter.org/
[21]: https://code.visualstudio.com/docs/editor/glob-patterns
[25]: https://mypy.readthedocs.io/en/stable/stubs.html
[26]: https://mypy.readthedocs.io/en/stable/index.html
[31]: https://www.youtube.com/watch?v=3S0RQdu5yV4
[32]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[33]: https://www.python.org/downloads/
[34]: https://www.anaconda.com/download/
[35]: https://marketplace.visualstudio.com/items?itemName=julialang.language-julia
[36]: https://julialang.org/downloads/
[37]: https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets
[38]: https://jupyter.org/install#jupyter-notebook
[39]: https://jupyter.org/install#jupyterlab
[40]: https://docs.jupyter.org/en/latest/install/notebook-classic.html
[41]: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
[42]: https://en.wikipedia.org/wiki/Project_Jupyter
[44]: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
[45]: https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
[46]: https://github.com/microsoft/vscode-jupyter/wiki/Setting-Up-Run-by-Line-and-Debugging-for-Notebooks
[47]: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode
[48]: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
[49]: https://en.wikipedia.org/w/index.php?title=Project_Jupyter&oldid=1214864300#Documents
[50]: https://realpython.com/python-repl/
[52]: https://code.visualstudio.com/blogs/2017/02/12/code-lens-roundup
[54]: https://github.com/nteract/papermill
[55]: https://github.com/jupyter/nbconvert
[56]: https://github.com/jupyter/nbgrader
[57]: https://revealjs.com/
[59]: https://ipython.readthedocs.io/en/stable/interactive/magics.html
[60]: https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server
[68]: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
[69]: https://code.visualstudio.com/docs/editor/port-forwarding
[70]: https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
[75]: https://github.com/microsoft/vscode/issues/116939
[76]: https://code.visualstudio.com/blogs/2021/07/06/workspace-trust
[78]: https://en.wikipedia.org/wiki/Symbol_table
[81]: https://en.wikipedia.org/wiki/Regular_expression
[84]: https://code.visualstudio.com/docs/sourcecontrol/overview#_timeline-view
[85]: https://code.visualstudio.com/docs/sourcecontrol/github
[88]: https://en.wikipedia.org/w/index.php?title=Bug_(engineering)&oldid=1230694591#History
[89]: https://en.wikipedia.org/w/index.php?title=Debugging&oldid=1224122939#Etymology
[90]: https://commons.wikimedia.org/w/index.php?title=File:First_Computer_Bug,_1945.jpg&oldid=868794824
[94]: https://www.youtube.com/watch?v=HzYKDfTMCtg
[95]: https://www.youtube.com/watch?v=xiE7ebXOqlY
[96]: https://code.visualstudio.com/docs/debugtest/debugging-configuration#_launchjson-attributes
[97]: https://code.visualstudio.com/docs/python/debugging#_set-configuration-options
[98]: https://code.visualstudio.com/api/advanced-topics/extension-host
[99]: https://marketplace.visualstudio.com/VSCode
[100]: https://code.visualstudio.com/docs/configure/keybindings#_command-arguments
[101]: https://www.youtube.com/watch?v=5tWJVLF6PuA
[104]: https://stackoverflow.com/questions/1552749/difference-between-cr-lf-lf-and-cr-line-break-types
[105]: https://github.com/microsoft/vscode/blob/main/LICENSE.txt
[106]: https://code.visualstudio.com/License/
[107]: https://github.com/microsoft/vscode/wiki/Differences-between-the-repository-and-Visual-Studio-Code
[108]: https://code.visualstudio.com/docs/editor/glob-patterns#_special-cases
[109]: https://code.visualstudio.com/docs/configure/keybindings#_running-multiple-commands
[112]: https://github.com/microsoft/vscode/wiki/How-to-Contribute#build-and-run
[113]: https://code.visualstudio.com/
[114]: https://github.com/microsoft/vscode
[115]: https://vscodium.com/
[118]: misc/exception_breakpoints.pptx
[141]: https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow
[142]: https://marketplace.visualstudio.com/items?itemName=Atlassian.atlascode
[182]: https://code.visualstudio.com/docs/editor/workspaces/multi-root-workspaces#_settings
[185]: https://git-scm.com/
[186]: https://code.visualstudio.com/docs/remote/ssh#_ssh-hostspecific-settings
[187]: https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence
[211]: https://code.visualstudio.com/docs/editor/keybindings#_keyboard-shortcuts-reference
[215]: https://code.visualstudio.com/docs/configure/keybindings#_conditional-operators
[221]: https://code.visualstudio.com/docs/configure/command-line
[222]: https://code.visualstudio.com/docs/copilot/overview
[223]: https://code.visualstudio.com/docs/configure/profiles
[224]: https://code.visualstudio.com/docs/remote/remote-overview
[225]: https://code.visualstudio.com/docs/editing/userdefinedsnippets
[226]: https://code.visualstudio.com/docs/debugtest/tasks
[228]: https://code.visualstudio.com/docs/setup/setup-overview#_how-big-is-vs-code
[229]: https://code.visualstudio.com/docs/configure/settings-sync
[231]: https://code.visualstudio.com/docs/configure/themes#_customize-a-color-theme
[233]: https://code.visualstudio.com/docs/editing/codebasics#_folding
[238]: https://code.visualstudio.com/docs/terminal/appearance
[239]: https://code.visualstudio.com/docs/terminal/profiles
[131]: https://code.visualstudio.com/docs/python/jupyter-support-py#_additional-commands-and-keyboard-shortcuts
[195]: https://code.visualstudio.com/docs/getstarted/userinterface#_customize-tab-labels
