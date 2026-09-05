export function submitChatOnEnter(event: KeyboardEvent, submit: () => void): boolean {
  if (event.key !== "Enter" || event.shiftKey || event.isComposing) return false;
  event.preventDefault();
  event.stopPropagation();
  submit();
  return true;
}
