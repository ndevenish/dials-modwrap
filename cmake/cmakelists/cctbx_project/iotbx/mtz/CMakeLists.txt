add_library ( iotbx_mtz 
            object.cpp
            crystal.cpp
            dataset.cpp
            column.cpp )
target_link_libraries(iotbx_mtz ccp4io cctbx iotbx)

add_python_library ( iotbx_mtz_ext
            ext.cpp
            object_bpl.cpp
            crystal_bpl.cpp
            dataset_bpl.cpp
            column_bpl.cpp
            batch_bpl.cpp )
target_link_libraries(iotbx_mtz_ext ccp4io cctbx iotbx_mtz scitbx_boost_python)

