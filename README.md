# Docs Generator
- This project uses MkDocs and a python script to organize project documentation into a single site
- The generated site uses GitHub pages and can be easily shared
- The project also uses NPM scripts to automate the overall process
- The only requriements other than installing MkDocs is to have python and pip available on your computer
- Please read the MkDocs [getting started](https://www.mkdocs.org/#getting-started) guide for more
- This project also uses the [Angular Material](https://github.com/angular/material2) project as an example.  The project downloads a local copy and collects all the markdown files from the project and creates an MkDocs site from that.  To change this just go into the npm scripts and add your project repo, and also modify the python script to look for whatever values you want to organize your site around.
