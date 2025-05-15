from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'submitted_at')
    list_filter = ('status', 'request_type')
    search_fields = ('user__username', 'description')
    readonly_fields = ('submitted_at', 'updated_at')

    actions = ['mark_approved', 'mark_rejected']

    def mark_approved(self, request, queryset):
        queryset.update(status='resolved')  # or use 'approved' if you have that
        self.message_user(request, "Selected requests marked as resolved.")

    def mark_rejected(self, request, queryset):
        queryset.update(status='closed')  # or use 'rejected' if you have that
        self.message_user(request, "Selected requests marked as closed.")

    mark_approved.short_description = "Mark selected as Approved (Resolved)"
    mark_rejected.short_description = "Mark selected as Rejected (Closed)"
    
