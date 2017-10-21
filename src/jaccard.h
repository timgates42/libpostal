#ifndef JACCARD_H
#define JACCARD_H

#include <stdio.h>
#include <stdlib.h>

#include "collections.h"

double jaccard_similarity(khash_t(str_set) *s1, khash_t(str_set) *s2);

#endif