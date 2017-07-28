add_python_library ( dxtbx_model_ext
            beam.cc
            goniometer.cc
            kappa_goniometer.cc
            multi_axis_goniometer.cc
            panel.cc
            detector.cc
            scan.cc
            scan_helpers.cc
            crystal.cc
            parallax_correction.cc
            pixel_to_millimeter.cc
            experiment.cc
            experiment_list.cc
            model_ext.cc )
target_link_libraries(dxtbx_model_ext cctbx cbf TIFF::TIFF scitbx_boost_python)

