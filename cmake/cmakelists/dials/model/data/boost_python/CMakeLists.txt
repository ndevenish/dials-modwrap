add_python_library ( dials_model_data_ext
            image_volume.cc
            adjacency_list.cc
            shoebox.cc
            observation.cc
            prediction.cc
            pixel_list.cc
            ray.cc
            image.cc
            data_ext.cc )
target_link_libraries(dials_model_data_ext cctbx scitbx_boost_python)

