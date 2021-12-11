# Discogs Label Generator
<h3>Why the label generator?</h3>

<p> This app was created while working at the record store <a href="https://landfillrescueunit.com">Landfil Rescue Unit</a>. 
On the outer plastic sleeve of a record the owner would make a sticker with information from the music database Discogs about the record for buyers to see. 
They would manually enter all of the fields into a spreadsheet (artist name, album name, format type, year and country of release) and then print it out as a sticker.
This looked very tedious!</p>

<h3>What this label generator does</h3>
<p> This app uses the requests library to access the Discogs API. It puts the information into a pandas dataframe, and returns the information in a .csv file.
All of this done though a Tkinter gui<p>

<h3>How to install the app</h3>
<p>Dockerization in progress and will update here soon!<p>

<h3>How to use the app</h3>
<dl>
  <dt>Enter the Discogs release ID/s into the text box in the GUI</dt>
    <dd> Dicogs release can be found on the release page in the top right hand corner. Once finished adding the id’s click on the ‘Upload ID” button.  This creates a txt file of the releases. </dd>
  <dt>Click the  ‘Run Generator button</dt>
    <dd>This makes a call to the Discogs API for the requested information about the selected releases.</dd>
  <dt>Click the Open</dt>
    <dd>his adds the newly called information a .csv file as well as deletes the txt file.</dd>
</dl>


