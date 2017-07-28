add_python_library ( mmtbx_building_loop_closure_ext
            ccd_bpl.cpp )
target_link_libraries(mmtbx_building_loop_closure_ext iotbx_pdb cctbx scitbx_boost_python)

