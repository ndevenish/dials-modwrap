add_python_library ( mmtbx_bulk_solvent_ext
            bulk_solvent_ext.cpp
            bulk_solvent.cpp )
target_link_libraries(mmtbx_bulk_solvent_ext cctbx scitbx_boost_python)

