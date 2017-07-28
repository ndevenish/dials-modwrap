add_python_library ( dials_refinement_helpers_ext
            gallego_yezzi.cc
            gaussian_smoother.cc
            mahalanobis.cc
            outlier_helpers.cc
            parameterisation_helpers.cc
            refinement_ext.cc
            restraints_helpers.cc
            rtmats.cc )
target_link_libraries(dials_refinement_helpers_ext cctbx scitbx_boost_python)

