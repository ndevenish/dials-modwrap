add_python_library ( dials_array_family_flex_ext
            flex_binner.cc
            flex_centroid.cc
            flex_ext.cc
            flex_int6.cc
            flex_intensity.cc
            flex_observation.cc
            flex_prediction.cc
            flex_reflection_table.cc
            flex_shoebox.cc
            flex_shoebox_extractor.cc
            flex_unit_cell.cc )
target_link_libraries(dials_array_family_flex_ext cctbx scitbx_boost_python)

