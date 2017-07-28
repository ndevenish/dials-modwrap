add_executable(tst_accessors tst_accessors.cpp)
add_test(NAME tst_accessors COMMAND tst_accessors)

add_executable(tst_af_1 tst_af_1.cpp)
add_test(NAME tst_af_1 COMMAND tst_af_1)

add_executable(tst_af_2 tst_af_2.cpp)
add_test(NAME tst_af_2 COMMAND tst_af_2)

add_executable(tst_af_3 tst_af_3.cpp)
add_test(NAME tst_af_3 COMMAND tst_af_3)

add_executable(tst_af_4 tst_af_4.cpp)
add_test(NAME tst_af_4 COMMAND tst_af_4)

add_executable(tst_af_5 tst_af_5.cpp)
add_test(NAME tst_af_5 COMMAND tst_af_5)

add_executable(tst_mat3 tst_mat3.cpp)
add_test(NAME tst_mat3 COMMAND tst_mat3)

add_executable(tst_optional_copy tst_optional_copy.cpp)
add_test(NAME tst_optional_copy COMMAND tst_optional_copy)

add_executable(tst_ref_matrix_facet tst_ref_matrix_facet.cpp)
add_test(NAME tst_ref_matrix_facet COMMAND tst_ref_matrix_facet)

add_executable(tst_sym_mat3 tst_sym_mat3.cpp)
add_test(NAME tst_sym_mat3 COMMAND tst_sym_mat3)

add_executable(tst_unsigned_float_arithmetic tst_unsigned_float_arithmetic.cpp)
add_test(NAME tst_unsigned_float_arithmetic COMMAND tst_unsigned_float_arithmetic)

add_executable(tst_vec3 tst_vec3.cpp)
add_test(NAME tst_vec3 COMMAND tst_vec3)

add_subdirectory(boost_python)
