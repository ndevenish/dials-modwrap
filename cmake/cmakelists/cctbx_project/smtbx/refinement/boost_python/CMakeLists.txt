add_python_library ( smtbx_refinement_least_squares_ext
            least_squares_ext.cpp
            weighting_schemes.cpp
            least_squares.cpp )
target_link_libraries(smtbx_refinement_least_squares_ext cctbx smtbx_refinement_constraints scitbx_boost_python)

