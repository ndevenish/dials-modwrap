add_python_library ( smtbx_structure_factors_direct_ext
            ext.cpp
            standard_xray.cpp )
target_link_libraries(smtbx_structure_factors_direct_ext cctbx)

