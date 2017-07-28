add_python_library ( scitbx_fftpack_ext
            fftpack_ext.cpp )
target_link_libraries(scitbx_fftpack_ext omptbx scitbx_boost_python)

