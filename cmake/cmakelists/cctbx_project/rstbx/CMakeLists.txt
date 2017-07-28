project(rstbx)

add_library ( rstbx 
            dps_core/dps_core.cpp
            dps_core/directional_fft.cpp
            dps_core/direction.cpp
            indexing_api/indexing_api.cpp
            diffraction/ewald_sphere.cpp
            diffraction/partial_spot_position_partial_H.cpp )
target_link_libraries(rstbx annlib cctbx annlib_adaptbx)
target_include_directories(rstbx PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/${CMAKE_CURRENT_SOURCE_DIR}/..)


add_python_library ( rstbx_ext
            ext.cpp )
target_link_libraries(rstbx_ext cctbx rstbx scitbx_boost_python)

add_subdirectory(apps)
add_subdirectory(array_family)
add_subdirectory(bandpass)
add_subdirectory(bpcx)
add_subdirectory(diffraction)
add_subdirectory(indexing_api)
add_subdirectory(simage)
add_subdirectory(simulation)
add_subdirectory(symmetry)
