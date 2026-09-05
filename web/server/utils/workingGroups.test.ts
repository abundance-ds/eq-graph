import assert from "node:assert/strict";
import test from "node:test";
import {
  parseWorkingGroups,
  researchWorkingGroups,
} from "../../shared/utils/workingGroups";

test("keeps the comma in the dissemination category", () => {
  assert.deepEqual(
    parseWorkingGroups("Dissemination, OA fee, Others"),
    ["Dissemination, OA fee", "Others"],
  );
});

test("splits known research working groups", () => {
  assert.deepEqual(
    researchWorkingGroups("Valuation, Education and Outreach"),
    ["Valuation", "Education and Outreach"],
  );
  assert.deepEqual(researchWorkingGroups("Dissemination, OA fee"), []);
});

test("rejects an unknown working-group value", () => {
  assert.throws(() => parseWorkingGroups("Unknown group"));
});
