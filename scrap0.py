    # try: 
    # if request.method == "POST":
       
    #     return send_file(img_io, mimetype='image/jpeg')

            # return redirect("/downloads")
            # try:
                #return send_file("imageName", as_attachment=True, mimetype="image/jpeg", attachment_filename='imageName')
                #return send_file(imageName, mimetype=None, as_attachment=False, attachment_filename=None, add_etags=True, cache_timeout=None, conditional=False, last_modified=None)
                #send_from_directory(file_dir, filename, as_attachment=True, mimetype='application/pdf', attachment_filename=(str(filename) + '.pdf'))
            # except Exception as e:
            #     error = str(e)
            #     return render_template("error.html", error=error)

            
    # except Exception as e:
    #     error = str(e)
    #     return render_template("error.html", error=error)

    # @app.route('/return-files/')
# def return_files_tut():
    


# @app.route("/downloads")
# def download():
#     try:
#         return send_file("imageName", as_attachment=True, attachment_filename='imageName')
#     except Exception as e:
#         error = str(e)
#         return render_template("error.html", error=error)