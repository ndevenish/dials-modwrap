add_python_library ( dials_algorithms_spot_prediction_ext
            index_generator.cc
            pixel_labeller.cc
            pixel_to_miller_index.cc
            ray_intersection.cc
            ray_predictor.cc
            reeke_index_generator.cc
            reflection_predictor.cc
            rotation_angles.cc
            scan_varying_helpers.cc
            scan_varying_ray_predictor.cc
            spot_prediction_ext.cc
            stills_ray_predictor.cc )
target_link_libraries(dials_algorithms_spot_prediction_ext cctbx scitbx_boost_python)

